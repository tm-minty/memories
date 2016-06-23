"""Chaos watcher."""

import logging

from chaos.handler import ChaosHandler

from watchdog.events import FileSystemEventHandler


class ChaosWatcher(FileSystemEventHandler):
    """Watches files and calls handler methods depending on file type."""

    chaos_handler = ChaosHandler()

    def on_created(self, event):
        """On file created event listener."""
        logging.info('Created %s: %s' % (
            'directory' if event.is_directory else 'file',
            event.src_path
        ))

        if not event.is_directory:
            self.chaos_handler.file(event.src_path)
