import os
import shutil
import tempfile
import unittest

from dummy_file_generator import file_generator


class FileGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def assertFileSizesEqual(self, file_size_expected):
        for filename in os.listdir(self.test_dir):
            full_path = os.path.join(self.test_dir, filename)
            file_size_actual = os.path.getsize(full_path)
            self.assertEqual(
                file_size_expected, file_size_actual,
                'For file "%s", expected file size %d bytes, got %d bytes' %
                (full_path, file_size_expected, file_size_actual))

    def test_generates_no_files_on_initialization(self):
        file_prefix = os.path.join(self.test_dir, 'dummy-prefix-')
        self.generator = file_generator.FileGenerator(
            file_prefix, bytes_per_file=42)
        self.assertEqual([], os.listdir(self.test_dir))

    def test_generates_single_file(self):
        file_prefix = os.path.join(self.test_dir, 'dummy-prefix-')
        self.generator = file_generator.FileGenerator(
            file_prefix, bytes_per_file=42)

        self.generator.next_file()

        self.assertItemsEqual([
            'dummy-prefix-00000000.testfile',
        ], os.listdir(self.test_dir))
        self.assertFileSizesEqual(42)

    def test_generates_three_files(self):
        file_prefix = os.path.join(self.test_dir, 'dummy-prefix-')
        self.generator = file_generator.FileGenerator(
            file_prefix, bytes_per_file=1000)

        self.generator.next_file()
        self.generator.next_file()
        self.generator.next_file()

        self.assertItemsEqual([
            'dummy-prefix-00000000.testfile',
            'dummy-prefix-00000001.testfile',
            'dummy-prefix-00000002.testfile',
        ], os.listdir(self.test_dir))
        self.assertFileSizesEqual(1000)

    def test_generates_large_file(self):
        file_prefix = os.path.join(self.test_dir, 'dummy-prefix-')
        self.generator = file_generator.FileGenerator(
            file_prefix, bytes_per_file=10 * 1024 * 1024)

        self.generator.next_file()

        self.assertItemsEqual([
            'dummy-prefix-00000000.testfile',
        ], os.listdir(self.test_dir))
        self.assertFileSizesEqual(10 * 1024 * 1024)

    def test_reports_correct_bytes_per_file(self):
        self.assertEqual(5,
                         file_generator.FileGenerator(
                             'dummy-prefix-', bytes_per_file=5).bytes_per_file)
        self.assertEqual(97,
                         file_generator.FileGenerator(
                             'dummy-prefix-', bytes_per_file=97).bytes_per_file)
