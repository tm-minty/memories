#!/usr/bin/env python3

import os
import time

from watchdog.observers import Observer

import config
from chaos_watcher import ChaosWatcher

def main():
    if not os.path.exists(config.paths['chaos']):
        os.makedirs(config.paths['chaos'])

    if not os.path.exists(config.paths['order']):
        os.makedirs(config.paths['order'])

    observer = Observer()
    observer.schedule(ChaosWatcher(), config.paths['chaos'], recursive=True)
    observer.start()

    print('Watching chaos dir: ', config.paths['chaos'])

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == '__main__':
	main()