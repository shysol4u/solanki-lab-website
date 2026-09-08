"""Nonvisual publishing metadata; the approved page bodies remain unchanged."""
from pathlib import Path
from html import escape
from urllib.parse import urlsplit
import json

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / 'site-config.json').read_text())
BASE = CONFIG['site_url'].rstrip('/')
assert urlsplit(BASE).scheme == 'https' and urlsplit(BASE).netloc
COPYRIGHT = f"© {CONFIG['copyright_year']} Solanki Lab, South Dakota State University. All rights reserved."
PAGES = []


def metadata(filename, title, description):
    url = BASE + '/' + ('' if filename == 'index.html' else filename)
    PAGES.append(url)
    values = {
        'og:type': 'website', 'og:site_name': CONFIG['site_name'],
        'og:title': title + ' | Solanki Lab', 'og:description': description,
        'og:url': url,
    }
    result = f'<link rel="canonical" href="{escape(url, quote=True)}">'
    result += ''.join(f'<meta property="{key}" content="{escape(value, quote=True)}">' for key, value in values.items())
    result += '<meta name="twitter:card" content="summary">'
    result += f'<meta name="twitter:title" content="{escape(title + " | Solanki Lab", quote=True)}">'
    result += f'<meta name="twitter:description" content="{escape(description, quote=True)}">'
    result += f'<meta name="copyright" content="{escape(COPYRIGHT, quote=True)}">'
    return result


def write_support_files():
    output = ROOT / 'dist'
    (output / '.nojekyll').write_text('', encoding='utf-8')
    (output / 'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + BASE + '/sitemap.xml\n', encoding='utf-8')
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += ''.join('  <url><loc>' + escape(url) + '</loc></url>\n' for url in PAGES)
    (output / 'sitemap.xml').write_text(sitemap + '</urlset>\n', encoding='utf-8')
    (output / 'copyright.txt').write_text(
        COPYRIGHT + '\n\nThis notice applies to original Solanki Lab material to the extent the lab or its authors hold the relevant rights. '
        'Third-party figures, photographs, fonts, software, institutional branding, and trademarks remain the property of their respective owners. '
        'This notice does not claim ownership of third-party material or SDSU trademarks on behalf of the lab.\n\n'
        'Asset provenance and unresolved permission information are recorded in ASSET_SOURCES.md in the website source repository.\n',
        encoding='utf-8')
