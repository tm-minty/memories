#!/usr/bin/env python3

import logging
import os
import shutil
import sys

import config

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s %(message)s',
)


def main(argv):
    test_image = 'tests/data/DSC_1231.JPG'

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

if __name__ == '__main__':
    main(sys.argv[1:])
