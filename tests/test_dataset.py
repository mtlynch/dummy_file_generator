import unittest

import mock

from dummy_file_generator import dataset


class DatasetTest(unittest.TestCase):

    def setUp(self):
        self.mock_file_generator = mock.Mock()

    def test_generates_files_when_datset_size_is_multiple_of_file_size(self):
        type(self.mock_file_generator).bytes_per_file = mock.PropertyMock(
            return_value=5)

        dataset.generate(self.mock_file_generator, total_dataset_bytes=50)

        self.assertEqual(10, self.mock_file_generator.next_file.call_count)

    def test_generates_no_files_when_datset_size_is_zero(self):
        type(self.mock_file_generator).bytes_per_file = mock.PropertyMock(
            return_value=5)

        dataset.generate(self.mock_file_generator, total_dataset_bytes=0)

        self.assertEqual(0, self.mock_file_generator.next_file.call_count)

    def test_rounds_up_file_count_to_exceed_dataset_size(self):
        type(self.mock_file_generator).bytes_per_file = mock.PropertyMock(
            return_value=100)

        dataset.generate(self.mock_file_generator, total_dataset_bytes=101)

        self.assertEqual(2, self.mock_file_generator.next_file.call_count)
