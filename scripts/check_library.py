#!/usr/bin/env python3
"""Check library navigation; offline, no third-party dependencies.

Supports inline Markdown links used by this library. Does not validate remote
URLs, heading anchors, reference-style links, or technical claims.
"""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r'\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"\n]*")?\)')
FIELDS = ('Type', 'Use when', 'Expected output', 'Recheck before use')


def check(root, names):
    root = root.resolve()
    errors = []
    pages = [root / name for name in names if name.endswith('.md')]
    index_targets = set()
    for page in pages:
        if not page.exists() or page.is_symlink():
            continue  # Publication checker handles symlinks.
        content = page.read_text(encoding='utf-8')
        # Ignore fenced examples; links there are not navigation.
        prose = re.sub(r'(?ms)^```[^\n]*\n.*?^```[^\n]*$', '', content)
        for match in LINK.finditer(prose):
            url = urlsplit(match.group(1).strip('<>'))
            if url.scheme or url.netloc or not url.path:
                continue
            target = (page.parent / unquote(url.path)).resolve()
            label = str(page.relative_to(root))
            if not target.is_relative_to(root):
                errors.append(f'{label}: link escapes repository: {url.path}')
            elif not target.exists():
                errors.append(f'{label}: missing local link: {url.path}')
            elif page == root / 'INDEX.md':
                index_targets.add(target)
        if page.is_relative_to(root / 'docs'):
            header = content.split('\n## ', 1)[0]
            for field in FIELDS:
                if not re.search(rf'^- \*\*{re.escape(field)}:\*\* \S', header, re.M):
                    errors.append(f'{page.relative_to(root)}: missing entry field {field}')
            if not content.startswith('# '):
                errors.append(f'{page.relative_to(root)}: missing title')
    for page in pages:
        if page.exists() and page.is_relative_to(root / 'docs') and page.resolve() not in index_targets:
            errors.append(f'{page.relative_to(root)}: missing from INDEX.md')
    return errors


def main():
    names = subprocess.check_output(
        ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=ROOT
    ).decode().split('\0')
    errors = check(ROOT, sorted(set(names) - {''}))
    for error in errors:
        print(error)
    print('Library check failed.' if errors else 'Library navigation and entry checks passed.')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
