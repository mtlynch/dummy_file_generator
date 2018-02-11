import logging
import math

logger = logging.getLogger(__name__)


def generate(file_generator, total_dataset_bytes):
    files_to_generate = _calculate_file_count(total_dataset_bytes,
                                              file_generator.bytes_per_file)
    for i in range(files_to_generate):
        file_generator.next_file()
        logger.info('File generation is %.1f%% complete',
                    (100.0 * (i + 1)) / files_to_generate)


def _calculate_file_count(total_dataset_bytes, bytes_per_file):
    file_count = float(total_dataset_bytes) / float(bytes_per_file)
    return int(math.ceil(file_count))
