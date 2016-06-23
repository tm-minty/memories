#!/usr/bin/env python3

import getopt
import logging
import os
import shutil
import sys

import config

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s %(message)s',
)


def usage():
        print("""
Create test data.
-h, --help      Show this text
-d, --directories   Create directories sctructure for recursive directory scan tests
""")


def main(argv):
    create_directories = False

    # Arguments
    try:
        opts, args = getopt.getopt(argv, ':hd', ['directories', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-d', '--directories'):
            create_directories = True

    test_image = 'tests/data/DSC_1231.JPG'

    if not os.path.exists(config.paths['chaos']):
        os.makedirs(config.paths['chaos'])

    if not os.path.exists(config.paths['order']):
        os.makedirs(config.paths['order'])

    for file in os.listdir(config.paths['chaos']):
        file_path = os.path.join(config.paths['chaos'], file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            else:
                shutil.rmtree(file_path)
        except Exception as e:
            logging.error(e)

    shutil.copy2(test_image, config.paths['chaos'])

    if create_directories:
        directories = [
            'test',
            'photos',
            'photos/123',
            'photos/june',
            'other',
        ]

        for directory in directories:
            directory = os.path.join(config.paths['chaos'], directory)
            os.makedirs(directory)
            shutil.copy2(test_image, directory)

if __name__ == '__main__':
    main(sys.argv[1:])
