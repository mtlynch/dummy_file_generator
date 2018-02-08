#!/usr/bin/python2

import argparse
import logging
import os

import file_generator as fg
import dataset

logger = logging.getLogger(__name__)


def configure_logging():
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-15s %(levelname)-4s %(message)s',
        '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def main(args):
    configure_logging()
    logger.info('Started runnning')
    _ensure_output_dir_exists(os.path.dirname(args.output_prefix))
    dataset.generate(
        fg.FileGenerator(args.output_prefix, args.size_per_file),
        args.total_size)


def _ensure_output_dir_exists(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Dummy File Generator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-p',
        '--output_prefix',
        required=True,
        help='Path prefix for generated files')
    parser.add_argument(
        '-f',
        '--size_per_file',
        required=True,
        help='Size (in bytes) per file',
        type=int)
    parser.add_argument(
        '-t',
        '--total_size',
        required=True,
        help='Size (in bytes) for full dataset',
        type=int)
    main(parser.parse_args())
