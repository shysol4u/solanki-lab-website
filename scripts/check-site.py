"""Dependency-free checks for native pages, approved content, and portable URLs.

Use --preserve-v6 for initial deployment fidelity. Normal future builds may
change approved content; the immutable Version 6 baseline is not rewritten.
"""
from html.parser import HTMLParser
from pathlib import Path
from hashlib import sha256
from urllib.parse import urljoin, urlsplit, unquote
from zipfile import ZipFile
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
checks = 0


def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


class Node:
    def __init__(self, tag, attrs=(), parent=None):
        self.tag, self.attrs, self.parent, self.parts = tag, dict(attrs), parent, []

    def text(self):
        return ''.join(p.text() if isinstance(p, Node) else p for p in self.parts)

    def walk(self):
        yield self
        for p in self.parts:
            if isinstance(p, Node):
                yield from p.walk()


class Document(HTMLParser):
    def __init__(self, content):
        super().__init__(convert_charrefs=True)
        self.root = Node('document')
        self.stack = [self.root]
        self.feed(content)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.stack[-1])
        self.stack[-1].parts.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        require(len(self.stack) > 1 and self.stack[-1].tag == tag, f'Unbalanced HTML closing tag: {tag}')
        self.stack.pop()

    def handle_data(self, data):
        self.stack[-1].parts.append(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--preserve-v6', action='store_true')
    args = parser.parse_args()
    config = json.loads((ROOT / 'site-config.json').read_text())
    base = config['site_url'].rstrip('/') + '/'
    require(base.startswith('https://'), 'Production canonical URLs must use HTTPS')
    documents = {p.name: Document(p.read_text(encoding='utf-8')) for p in OUT.glob('*.html')}
    require(set(documents) == {'index.html', 'research.html', 'team.html', 'outreach.html',
                               'funding.html', 'recruitment.html', 'guidelines.html'}, 'All seven approved pages exist')
    total_references = 0
    for name, document in documents.items():
        nodes = list(document.root.walk())
        require(len(document.stack) == 1, f'Complete HTML tree: {name}')
        ids = [n.attrs['id'] for n in nodes if 'id' in n.attrs]
        require(len(ids) == len(set(ids)), f'Unique page anchors: {name}')
        require(sum(n.tag == 'h1' for n in nodes) == 1, f'One primary heading: {name}')
        require(any(n.tag == 'meta' and n.attrs.get('name') == 'viewport' for n in nodes), f'Responsive viewport: {name}')
        require(any(n.tag == 'title' and n.text().strip() for n in nodes), f'Page title: {name}')
        expected_url = base + ('' if name == 'index.html' else name)
        require(any(n.tag == 'link' and n.attrs.get('rel') == 'canonical' and n.attrs.get('href') == expected_url for n in nodes),
                f'Canonical URL matches deployment path: {name}')
        for prop in ['og:title', 'og:description', 'og:url', 'og:site_name']:
            require(any(n.tag == 'meta' and n.attrs.get('property') == prop and n.attrs.get('content') for n in nodes),
                    f'Social metadata {prop}: {name}')
        guideline_links = [n for n in nodes if n.tag == 'a' and n.text().strip() == 'Lab Guidelines']
        require(guideline_links and all(n.attrs.get('href') == 'guidelines.html' and 'target' not in n.attrs for n in guideline_links),
                f'Guidelines menu remains an internal native-page link: {name}')
        for node in nodes:
            if node.tag == 'img':
                require('alt' in node.attrs, f'Image alt attribute: {name}')
                require(node.attrs.get('width') and node.attrs.get('height'), f'Stable image dimensions: {name}')
            for attr in ['href', 'src', 'data']:
                value = node.attrs.get(attr)
                if not value:
                    continue
                url = urlsplit(value)
                if url.scheme or url.netloc:
                    continue
                target = OUT / unquote(url.path) if url.path else OUT / name
                require(not url.path.startswith('/'), f'Project-site URL must remain relative: {name} -> {value}')
                require(target.is_file(), f'Local asset/page exists: {name} -> {value}')
                resolved = urljoin(base + name, value)
                require(resolved.startswith(base), f'Relative link stays under GitHub Pages project path: {value}')
                if url.fragment and target.suffix == '.html':
                    require(any(n.attrs.get('id') == unquote(url.fragment) for n in documents[target.name].root.walk()),
                            f'Local anchor exists: {name} -> {value}')
                total_references += 1
    guidelines = list(documents['guidelines.html'].root.walk())
    require(not any(n.tag in {'object', 'embed', 'iframe'} for n in guidelines), 'Guidelines has no embedded document viewer')
    mapped = [n for n in guidelines if 'data-source-block' in n.attrs]
    W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
    with ZipFile(ROOT / 'docs/Solanki_Lab_FGPMSI_V1-source.docx') as package:
        xml = ET.fromstring(package.read('word/document.xml'))
    expected = []
    for index, paragraph in enumerate(xml.find(W + 'body')):
        if paragraph.tag != W + 'p':
            continue
        pieces = []
        for run in paragraph.iter(W + 'r'):
            for node in run.iter():
                if node.tag == W + 't':
                    pieces.append(node.text or '')
                elif node.tag == W + 'tab':
                    pieces.append('\t')
                elif node.tag == W + 'br' and node.get(W + 'type') != 'page':
                    pieces.append('\n')
        text = ''.join(pieces)
        if text.strip() or paragraph.find('.//' + A + 'blip') is not None:
            expected.append((index, text))
    require([(int(n.attrs['data-source-block']), n.text()) for n in mapped] == expected,
            'Every meaningful Guidelines source block matches exactly and appears in source order')
    for node in mapped:
        ancestor = node.parent
        while ancestor:
            require(ancestor.tag != 'details' and 'hidden' not in ancestor.attrs, 'Guidelines content is directly readable')
            ancestor = ancestor.parent
    css = (OUT / 'style.css').read_text() + (OUT / 'guidelines.css').read_text()
    require('prefers-reduced-motion' in css and 'focus-visible' in css, 'Reduced-motion and keyboard-focus styles remain present')
    require('overflow-x: auto' in css and 'white-space: pre' in css, 'Technical commands retain horizontal code scrolling')
    for filename in ['robots.txt', 'sitemap.xml', 'copyright.txt', '.nojekyll']:
        require((OUT / filename).is_file(), f'Publishing support file exists: {filename}')
    sitemap = ET.parse(OUT / 'sitemap.xml')
    locations = {n.text for n in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
    require(locations == {base + ('' if p == 'index.html' else p) for p in documents}, 'Sitemap contains all seven canonical pages')
    files = [p for p in OUT.rglob('*') if p.is_file()]
    require(not any(p.is_symlink() for p in OUT.rglob('*')), 'Static deployment has no symlinks')
    require(sum(p.stat().st_size for p in files) < 1024**3, 'Published website is below the GitHub Pages size limit')
    require(not any(p.name.startswith('.env') or p.suffix in {'.key', '.pem', '.bundle'} for p in files),
            'No secret/configuration backup files are in public assets')
    fidelity = None
    if args.preserve_v6:
        baseline = json.loads((ROOT / 'audit/approved-v6.json').read_text())['files']
        for name, expected_file in baseline.items():
            data = (OUT / name).read_bytes()
            if name.endswith('.html'):
                require(sha256(data[data.index(b'<body'):]).hexdigest() == expected_file['body_sha256'],
                        f'Approved visible HTML, navigation, scripts and page body preserved: {name}')
            else:
                require(sha256(data).hexdigest() == expected_file['sha256'], f'Approved asset bytes preserved: {name}')
        require({str(p.relative_to(OUT)) for p in files} - set(baseline) ==
                {'.nojekyll', 'robots.txt', 'sitemap.xml', 'copyright.txt'}, 'Only nonvisual publishing support files added')
        fidelity = {'approved_page_bodies_unchanged': 7, 'approved_non_html_files_unchanged': len(baseline) - 7,
                    'only_head_metadata_and_support_files_added': True}
    report = {'status': 'passed', 'checks_passed': checks, 'pages': len(documents),
              'local_references': total_references, 'guidelines_source_blocks': len(expected),
              'public_bytes': sum(p.stat().st_size for p in files), 'migration_fidelity': fidelity,
              'browser_testing': 'Not performed by this source checker. This does not verify deployed HTTPS or real device rendering.'}
    (ROOT / 'audit/latest-check.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
