# Dummy File Generator

[![Build Status](https://travis-ci.org/mtlynch/dummy_file_generator.svg?branch=master)](https://travis-ci.org/mtlynch/dummy_file_generator)
[![Coverage Status](https://coveralls.io/repos/github/mtlynch/dummy_file_generator/badge.svg?branch=master)](https://coveralls.io/github/mtlynch/dummy_file_generator?branch=master)
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](LICENSE)

## Overview

Dummy File Generator generates files containing random data. The user can specify the number of bytes per file and the total amount of data to fill. Dummy File Generator will generate enough files to meet or exceed the total data amount specified.

## Example Usage

The example below demonstrates using the dummy file generator to generate 250 MiB of dummy files, made up of files of size 50 MiB each:

```
$ python dummy_file_generator/main.py \
  --size_per_file 52428800 \
  --total_size 262144000 \
  --output_prefix /tmp/test1/dummy-test-
```

```
$ du -h /tmp/test1/*
50M     /tmp/test1/dummy-test-00000000.testfile
50M     /tmp/test1/dummy-test-00000001.testfile
50M     /tmp/test1/dummy-test-00000002.testfile
50M     /tmp/test1/dummy-test-00000003.testfile
50M     /tmp/test1/dummy-test-00000004.testfile
```

