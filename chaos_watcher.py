from watchdog.events import FileSystemEventHandler

class ChaosWatcher(FileSystemEventHandler):
	def __init__(self):
		super()
		print('Hello, I\'m ChaosWatcher')

	def on_created(self, event):
		print('Created %s: %s' % (
			'directory' if event.is_directory else 'file',
			event.src_path
			))