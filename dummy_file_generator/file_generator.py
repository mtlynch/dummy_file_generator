import logging
import os
import tempfile

logger = logging.getLogger(__name__)


class FileGenerator(object):
    """Generates files containing random bytes."""

    def __init__(self, file_prefix, bytes_per_file):
        """Creates a new FileGenerator instance.

        Args:
            file_prefix: Path prefix for generated files. For example, a prefix:
                    '/tmp/test1234-'
                will yield test files like:
                    /tmp/test-1234-00000000.testfile
                    /tmp/test-1234-00000001.testfile
                    /tmp/test-1234-00000002.testfile
            bytes_per_file: The number of bytes to write to each output file.
        """
        self._file_prefix = file_prefix
        self._bytes_per_file = bytes_per_file
        self._files_generated = 0

    def next_file(self):
        """Generates the next dummy file and write it to disk."""
        filename = '%s%08d.testfile' % (self._file_prefix,
                                        self._files_generated)
        logger.info('Creating file: %s', filename)
        temp_file_handle, temp_filename = tempfile.mkstemp()
        with os.fdopen(temp_file_handle, 'wb') as temp_file:
            _write_n_bytes(temp_file, self._bytes_per_file)
        os.rename(temp_filename, filename)
        self._files_generated += 1

    @property
    def bytes_per_file(self):
        """Returns the number of bytes generator writes to each file."""
        return self._bytes_per_file


def _write_n_bytes(output_file, bytes_to_write):
    """Writes N bytes to the given file.

    Args:
        output_file: Destination file handle to write bytes.
        bytes_to_write: Number of bytes to write to file.
    """
    bytes_left = bytes_to_write
    while bytes_left > 0:
        next_chunk = min(4 * 1024 * 1024, bytes_left)
        output_file.write(os.urandom(next_chunk))
        bytes_left -= next_chunk
