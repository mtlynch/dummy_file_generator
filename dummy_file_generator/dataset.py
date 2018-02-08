import math


def generate(file_generator, total_dataset_bytes):
    files_to_generate = _calculate_file_count(total_dataset_bytes,
                                              file_generator.bytes_per_file)
    for _ in range(files_to_generate):
        file_generator.next_file()


def _calculate_file_count(total_dataset_bytes, bytes_per_file):
    file_count = float(total_dataset_bytes) / float(bytes_per_file)
    return int(math.ceil(file_count))
