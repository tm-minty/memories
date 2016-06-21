import os
from datetime import datetime

from gi.repository import GExiv2

import config

class ChaosHandler():
	def __init__(self):
		print('Hello, I\'m ChaosHandler')

	def image(self, path):
		print('image %s' % path)

		exif = GExiv2.Metadata(path)

		for p in dir(exif):
			print(p)

		created_at = exif.get_date_time()

		move_to = os.path.join(
			config.paths['order'], 
			'%04d' % created_at.year, 
			'%02d' % created_at.month, 
			'%02d' % created_at.day,
			)

		if not os.path.exists(move_to):
			os.makedirs(move_to)
			
		os.rename(path, os.path.join(move_to, os.path.basename(path)))
