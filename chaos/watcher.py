import logging
import mimetypes

from chaos.handler import ChaosHandler

import config

from watchdog.events import FileSystemEventHandler


class ChaosWatcher(FileSystemEventHandler):
    chaos_handler = ChaosHandler()

    def on_created(self, event):
        logging.info('Created %s: %s' % (
            'directory' if event.is_directory else 'file',
            event.src_path
        ))

        if not event.is_directory:
            mimetype, encoding = mimetypes.guess_type(event.src_path)

            logging.info('MimeType: %s' % (
                mimetype if mimetype else 'unknown'
            ))

            if mimetype in config.types['images']:
                self.chaos_handler.image(event.src_path)

    # DEBUG ONLY
    def on_modified(self, event):
        if config.DEBUG:
            self.on_created(event)
