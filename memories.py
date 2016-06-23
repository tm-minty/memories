#!/usr/bin/env python3

import getopt
import logging
import os
import sys
import time

from chaos.watcher import ChaosWatcher

import config

from watchdog.observers import Observer


def usage():
    print("""
Memories. Usage.
-h, --help      Show this text
-V, --verbose   Verbose logging level
-l, --log       Save debug information to log file
""")


def scan_files(directory):
    f = []
    for root, subdirs, files in os.walk(directory):
        for file in files:
            f.append(os.path.join(root, file))

    return f


def main(argv):
    log_file = config.log_file
    debug_level = config.debug_level

    # Arguments
    try:
        opts, args = getopt.getopt(argv, 'l:hV', ['log', 'help', 'verbose'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-V', '--verbose'):
            debug_level = logging.INFO
        elif opt in ('-l', '--log'):
            debug_level = logging.INFO
            log_file = arg

    logging.basicConfig(
        level=debug_level,
        filename=log_file,
        format='%(levelname)s: %(asctime)s %(message)s',
    )

    if not os.path.exists(config.paths['chaos']):
        os.makedirs(config.paths['chaos'])

    if not os.path.exists(config.paths['order']):
        os.makedirs(config.paths['order'])

    watcher = ChaosWatcher()

    logging.info('Scanning chaos dir...')
    initial_files = scan_files(config.paths['chaos'])
    for file in initial_files:
        watcher.chaos_handler.file(file)

    observer = Observer()
    observer.schedule(watcher, config.paths['chaos'], recursive=True)
    observer.start()

    logging.info('Watching chaos dir: %s' % config.paths['chaos'])

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == '__main__':
    main(sys.argv[1:])
