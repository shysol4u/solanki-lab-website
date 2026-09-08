"""Render only the approved V6 guidelines, directly from the supplied DOCX.

The explicit heading map records the source's manually styled hierarchy.
No policy text is maintained separately from the authoritative document.
"""
from html import escape
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/Solanki_Lab_FGPMSI_V1-source.docx'
SOURCE_SHA256 = '0ac9579569eccbae3eb708694ab902a3aca56ca11e60c61a6552d6acb6980446'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
NS = {'w': W[1:-1], 'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
HEADINGS = {
    2: (1, 'Solanki Lab'),
    4: (2, '1. Lab Philosophy'),
    7: (2, '2. Open-Door Policy'),
    13: (2, '3. Communication and Email'),
    22: (2, '4. Lab Meetings'),
    34: (2, '5. Lab Etiquette and Shared Responsibilities'),
    44: (3, 'Lab Police'),
    58: (2, '6. Expectations'),
    69: (2, '7. Scientific Independence and Teamwork'),
    80: (2, '8. Larger Equipment and Shared Facilities'),
    82: (3, 'BZX-1000 and Imaris'),
    89: (3, 'Greenhouse Use'),
    97: (3, 'Growth Chamber and Misting Chamber Use'),
    106: (2, '9. Research Records and Data'),
    123: (2, '10. HPC Data Storage and Transfer'),
    127: (3, 'Computer to HPC Using MobaXterm and rsync (alternate: FileZilla, Putty)'),
    154: (3, 'Globus Transfers'),
    156: (3, 'General HPC Data Expectations'),
    164: (2, '11. Authorship and Scientific Credit'),
    174: (2, '12. Safety and Compliance'),
    184: (2, '13. Professional Development'),
}
CODE_GROUPS = {
    125: ([125], 'Solanki Lab data-transfer directory'),
    130: ([130, 131, 132], 'Windows drives in MobaXterm'),
    134: ([134, 135], 'Example source path'),
    145: (list(range(145, 153)), 'Typical transfer command'),
}


def source_text(element):
    parts = []
    # Paragraph tab-stop definitions are layout metadata, not literal text tabs.
    nodes = (node for run in element.iter(W + 'r') for node in run.iter()) if element.tag == W + 'p' else element.iter()
    for node in nodes:
        if node.tag == W + 't':
            parts.append(node.text or '')
        elif node.tag == W + 'tab':
            parts.append('\t')
        elif node.tag == W + 'cr':
            parts.append('\n')
        elif node.tag == W + 'br' and node.get(W + 'type') != 'page':
            parts.append('\n')
        elif node.tag == W + 'noBreakHyphen':
            parts.append('\u2011')
    return ''.join(parts)


def enabled(properties, name):
    prop = properties.find(W + name) if properties is not None else None
    return prop is not None and prop.get(W + 'val') not in ('0', 'false', 'off')


def inline(paragraph, heading=False):
    """Preserve text and meaningful run formatting; activate literal source URLs."""
    groups = []
    for run in paragraph.iter(W + 'r'):
        text = source_text(run)
        if not text:
            continue
        properties = run.find(W + 'rPr')
        font = properties.find(W + 'rFonts') if properties is not None else None
        code = font is not None and font.get(W + 'ascii') == 'Consolas'
        style = (enabled(properties, 'b') and not heading,
                 enabled(properties, 'i'), code, enabled(properties, 'u'))
        if groups and groups[-1][0] == style:
            groups[-1] = (style, groups[-1][1] + text)
        else:
            groups.append((style, text))
    result = []
    for (bold, italic, code, underline), text in groups:
        if code:
            content = '<code>' + escape(text) + '</code>'
        else:
            pieces = re.split(r'(https?://[^\s<>]+)', text)
            content = ''.join(
                f'<a href="{escape(piece, quote=True)}">{escape(piece)}</a>'
                if re.match(r'^https?://', piece) else escape(piece)
                for piece in pieces
            ).replace('\n', '<br>')
        if italic:
            content = '<em>' + content + '</em>'
        if underline:
            content = '<u>' + content + '</u>'
        if bold:
            content = '<strong>' + content + '</strong>'
        result.append(content)
    return ''.join(result)


def heading_id(index):
    if index == 2:
        return 'guidelines-document-title'
    title = re.sub(r'^\d+\.\s*', '', HEADINGS[index][1])
    return 'guidelines-' + re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')


def contents():
    items = []
    subsection_open = False
    section_open = False
    for index, (level, title) in HEADINGS.items():
        if level == 1:
            continue
        link = f'<a href="#{heading_id(index)}">{escape(title)}</a>'
        if level == 2:
            if subsection_open:
                items.append('</ol>')
                subsection_open = False
            if section_open:
                items.append('</li>')
            items.append('<li>' + link)
            section_open = True
        else:
            if not subsection_open:
                items.append('<ol role="list">')
                subsection_open = True
            items.append('<li>' + link + '</li>')
    if subsection_open:
        items.append('</ol>')
    if section_open:
        items.append('</li>')
    return ('<details class="guidelines-toc"><summary id="guidelines-contents-label">'
            'Contents</summary><nav aria-labelledby="guidelines-contents-label">'
            '<ol role="list">' + ''.join(items) + '</ol></nav></details>')


def build_guidelines():
    raw = SOURCE.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SOURCE_SHA256:
        raise ValueError('Guidelines source changed. Review its complete structure before updating the conversion map.')
    with ZipFile(SOURCE) as package:
        document = ET.fromstring(package.read('word/document.xml'))
        numbering = ET.fromstring(package.read('word/numbering.xml'))
    body = list(document.find(W + 'body'))
    assert len(body) == 199
    assert not document.findall('.//w:tbl', NS), 'A new source table needs a reviewed conversion.'
    assert len(document.findall('.//a:blip', NS)) == 1
    assert not document.findall('.//w:hyperlink', NS), 'Review new source hyperlinks before conversion.'
    for index, (_, title) in HEADINGS.items():
        assert source_text(body[index]).strip() == title, f'Heading changed at source block {index}'
    for index, element in enumerate(body):
        assert element.tag in (W + 'p', W + 'sectPr'), f'Unreviewed source element at {index}'

    list_formats = {}
    for number in numbering.findall(W + 'num'):
        num_id = number.get(W + 'numId')
        abstract_id = number.find(W + 'abstractNumId').get(W + 'val')
        abstract = next(n for n in numbering.findall(W + 'abstractNum')
                        if n.get(W + 'abstractNumId') == abstract_id)
        level = next(n for n in abstract.findall(W + 'lvl') if n.get(W + 'ilvl') == '0')
        assert level.find(W + 'numFmt').get(W + 'val') == 'bullet'
        list_formats[num_id] = level.find(W + 'lvlText').get(W + 'val')

    output = ['<div class="wrap guidelines-page"><p class="eyebrow">LAB GUIDELINES</p>',
              '<article class="guidelines-document" aria-labelledby="guidelines-document-title">',
              '<header class="guidelines-document-header">']
    manifest = []
    empty = []
    active_list = None
    consumed = set()
    for index, paragraph in enumerate(body):
        if index in consumed or paragraph.tag == W + 'sectPr':
            continue
        text = source_text(paragraph)
        image = paragraph.find('.//a:blip', NS)
        if not text.strip() and image is None:
            empty.append(index)
            continue
        num = paragraph.find('w:pPr/w:numPr', NS)
        num_id = num.find(W + 'numId').get(W + 'val') if num is not None else None
        if num is not None:
            assert num.find(W + 'ilvl').get(W + 'val') == '0'
        if active_list and active_list != num_id:
            output.append('</ul>')
            active_list = None
        if num_id and not active_list:
            marker_class = {'\uf076': 'guidelines-diamond-list', '\uf0d8': 'guidelines-arrow-list'}.get(list_formats[num_id], '')
            output.append(f'<ul data-word-num-id="{num_id}" class="{marker_class}">')
            active_list = num_id
        attributes = f'data-source-block="{index}"'
        if image is not None:
            assert index == 0 and not text.strip()
            output.append(f'<figure class="guidelines-source-logo" {attributes}>'
                          '<img src="assets/guidelines/solanki-lab-source-logo.png" width="401" height="370" '
                          'alt="Solanki Lab FG-PMSI logo: a blue triangular emblem with an S, a plant, and a DNA helix." '
                          'decoding="async"></figure>')
            role = 'image'
        elif index in HEADINGS:
            level = HEADINGS[index][0]
            output.append(f'<h{level} id="{heading_id(index)}" {attributes}>{inline(paragraph, heading=True)}</h{level}>')
            role = f'h{level}'
        elif index in CODE_GROUPS:
            indices, label = CODE_GROUPS[index]
            lines = []
            for line_index in indices:
                line_text = source_text(body[line_index])
                lines.append(f'<span data-source-block="{line_index}">{escape(line_text)}</span>')
                manifest.append({'block': line_index, 'kind': 'code-line', 'text': line_text})
                consumed.add(line_index)
            output.append(f'<pre class="guidelines-code" tabindex="0" role="region" aria-label="{escape(label)}">'
                          '<code>' + '\n'.join(lines) + '</code></pre>')
            continue
        else:
            tag = 'li' if num_id else 'p'
            cls = ' class="guidelines-subtitle"' if index == 3 else ''
            output.append(f'<{tag}{cls} {attributes}>{inline(paragraph)}</{tag}>')
            role = tag
        entry = {'block': index, 'kind': role, 'text': text}
        if num_id:
            entry.update({'list_id': num_id, 'list_level': 0, 'source_marker': list_formats[num_id]})
        manifest.append(entry)
        if index == 3:
            output.append('</header>')
            output.append(contents())
            output.append('<p class="guidelines-download"><a href="files/Solanki_Lab_FGPMSI.pdf?v6-20260907" '
                          'download="Solanki_Lab_Guidelines.pdf">Download Lab Guidelines as PDF</a></p>')
    if active_list:
        output.append('</ul>')
    output.append('</article></div>')
    (ROOT / 'docs/guidelines-v6-source-map.json').write_text(json.dumps({
        'source': SOURCE.name,
        'source_sha256': SOURCE_SHA256,
        'source_body_blocks': len(body),
        'omitted_empty_paragraphs': empty,
        'blocks': manifest,
    }, indent=2, ensure_ascii=False) + '\n')
    return '\n'.join(output)
