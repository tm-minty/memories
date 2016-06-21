#!/usr/bin/env python3

import logging
import os
import time

from chaos.watcher import ChaosWatcher

import config

from watchdog.observers import Observer


def main():
    logging.basicConfig(level=logging.DEBUG)

    if not os.path.exists(config.paths['chaos']):
        os.makedirs(config.paths['chaos'])

    if not os.path.exists(config.paths['order']):
        os.makedirs(config.paths['order'])

    observer = Observer()
    observer.schedule(ChaosWatcher(), config.paths['chaos'], recursive=True)
    observer.start()

    logging.info('Watching chaos dir: %s' % config.paths['chaos'])

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == '__main__':
    main()
