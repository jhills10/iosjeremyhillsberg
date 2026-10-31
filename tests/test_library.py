"""Exercise navigation failure cases without touching the working library."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('check_library', Path(__file__).resolve().parents[1] / 'scripts/check_library.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'docs').mkdir()
        (self.root / 'INDEX.md').write_text('[Guide](docs/guide.md)\n')
        self.page = self.root / 'docs/guide.md'
        self.page.write_text('# Guide\n\n' + ''.join(f'- **{field}:** Example\n' for field in module.FIELDS))
        self.names = ['INDEX.md', 'docs/guide.md']

    def test_valid_and_external_links(self):
        with self.page.open('a') as file:
            file.write('\n[Index](../INDEX.md) [Web](https://example.com/no-local-file)\n')
        self.assertEqual(module.check(self.root, self.names), [])

    def test_missing_and_escaping_links(self):
        with self.page.open('a') as file:
            file.write('\n[Missing](missing.md) [Outside](../../outside.md)\n')
        errors = module.check(self.root, self.names)
        self.assertTrue(any('missing local link' in e for e in errors))
        self.assertTrue(any('escapes repository' in e for e in errors))

    def test_unindexed_and_missing_fields(self):
        (self.root / 'INDEX.md').write_text('# Index\n')
        self.page.write_text('# Guide\n')
        errors = module.check(self.root, self.names)
        self.assertTrue(any('missing from INDEX' in e for e in errors))
        self.assertEqual(sum('missing entry field' in e for e in errors), 4)

    def test_fenced_example_is_not_a_link(self):
        with self.page.open('a') as file:
            file.write('\n```md\n[Example](missing.md)\n```\n')
        self.assertEqual(module.check(self.root, self.names), [])
