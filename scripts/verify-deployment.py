"""Read-only verification of an actually deployed, public HTTPS website.

Run after GitHub reports a successful deployment, in a network-capable
environment. This compares served bytes; it does not replace browser QA.
"""
from pathlib import Path
from hashlib import sha256
from urllib.parse import urlsplit, urljoin
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from concurrent.futures import ThreadPoolExecutor
import argparse
import json

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='The verified deployment URL returned by GitHub Pages')
    args = parser.parse_args()
    base = args.url.rstrip('/') + '/'
    if urlsplit(base).scheme != 'https':
        parser.error('Use the actual HTTPS production URL.')
    configured = json.loads((ROOT / 'site-config.json').read_text())['site_url'].rstrip('/') + '/'
    if base != configured:
        parser.error('The deployed URL differs from site-config.json. Confirm the actual domain and update/rebuild metadata first.')
    paths = [p for p in sorted((ROOT / 'dist').rglob('*')) if p.is_file() and not p.name.startswith('.')]

    def verify(path):
        relative = path.relative_to(ROOT / 'dist').as_posix()
        expected = path.read_bytes()
        target = urljoin(base, '' if relative == 'index.html' else relative)
        request = Request(target, headers={'User-Agent': 'SolankiLab-Deployment-Verification/6', 'Cache-Control': 'no-cache'})
        try:
            with urlopen(request, timeout=30) as response:
                final_url = response.geturl()
                received = response.read()
                public_https = response.status == 200 and final_url.startswith(base)
                matches = sha256(received).digest() == sha256(expected).digest()
                return {'file': relative, 'status': response.status, 'public_https': public_https,
                        'exact_bytes': matches, 'passed': public_https and matches}
        except (HTTPError, URLError, TimeoutError) as error:
            return {'file': relative, 'passed': False, 'error': str(error)}

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(verify, paths))
    passed = all(r['passed'] for r in results)
    report = {'status': 'passed' if passed else 'failed', 'url': base, 'files_checked': len(results),
              'results': results, 'browser_testing': 'Not covered by this HTTPS/byte comparison.'}
    (ROOT / 'audit/deployment-check.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
