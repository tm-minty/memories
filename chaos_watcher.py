import mimetypes

from chaos_handler import ChaosHandler

import config

from watchdog.events import FileSystemEventHandler


class ChaosWatcher(FileSystemEventHandler):
    chaos_handler = ChaosHandler()

    def __init__(self):
        super()
        print('Hello, I\'m ChaosWatcher')

    def on_created(self, event):
        print('Created %s: %s' % (
            'directory' if event.is_directory else 'file',
            event.src_path
        ))
        if not event.is_directory:
            mimetype, encoding = mimetypes.guess_type(event.src_path)
            print('with mime type: %s' % (
                mimetype if mimetype else 'unknown'
            ))

            if mimetype in config.types['images']:
                self.chaos_handler.image(event.src_path)

    def on_modified(self, event):
        self.on_created(event)
