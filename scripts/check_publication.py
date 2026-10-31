#!/usr/bin/env python3
"""Conservative working-tree publication checks. Not a confidentiality audit."""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ALLOWED = {'.md', '.txt', '.swift', '.py', '.yml', '.yaml', '.json'}
SPECIAL = {'.gitignore', 'LICENSE', 'NOTICE'}
PATTERNS = {
    'private key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----'),
    'GitHub token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b'),
    'AWS access key': re.compile(r'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b'),
    'credential assignment': re.compile(
        r'''(?i)\b(?:api[_-]?key|client[_-]?secret|password|access[_-]?token)\s*[:=]\s*["']([^"'\r\n]{8,})["']'''),
}
PLACEHOLDERS = {'YOUR_API_KEY', 'YOUR_TOKEN', 'PLACEHOLDER', 'EXAMPLE_ONLY', 'REPLACE_ME'}


def findings(path):
    if path.is_symlink():
        return [(0, 'symlink requires review')]
    if path.name.startswith('.env') or (path.suffix not in ALLOWED and path.name not in SPECIAL):
        return [(0, 'file type requires publication review')]
    if path.stat().st_size > 512_000:
        return [(0, 'file exceeds 512 KB review threshold')]
    try:
        content = path.read_text(encoding='utf-8')
    except UnicodeError:
        return [(0, 'non-UTF-8 content requires review')]
    if '\x00' in content:
        return [(0, 'binary content requires review')]
    result = []
    for number, line in enumerate(content.splitlines(), 1):
        for category, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                if category == 'credential assignment' and match.group(1) in PLACEHOLDERS:
                    continue
                result.append((number, category))
    return result


def main():
    names = subprocess.check_output(
        ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=ROOT
    ).decode().split('\0')
    failed = False
    for name in sorted(set(names) - {''}):
        path = ROOT / name
        if not path.exists() and not path.is_symlink():
            continue  # Deleted files have no working-tree content to inspect.
        for line, category in findings(path):
            # Never echo matched content; filenames are escaped to prevent log injection.
            print(f'{ascii(name)}:{line}: {category}')
            failed = True
    if failed:
        print('Publication check failed. Review findings before publishing.')
        return 1
    print('Publication check passed. Human provenance and privacy review still required.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
