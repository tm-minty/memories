#!/usr/bin/env python3

import os
import time

from watchdog.observers import Observer

import config
from chaos_watcher import ChaosWatcher

def main():
    if not os.path.exists(config.watcher['chaos']):
        os.makedirs(config.watcher['chaos'])

    if not os.path.exists(config.watcher['order']):
        os.makedirs(config.watcher['order'])

    observer = Observer()
    observer.schedule(ChaosWatcher(), config.watcher['chaos'], recursive=True)
    observer.start()

    print('Watching chaos dir: ', config.watcher['chaos'])

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == '__main__':
	main()