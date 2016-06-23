"""Chaos handler."""

import logging
import mimetypes
import os
import shutil

import config

import gi
gi.require_version('GExiv2', '0.10')
from gi.repository import GExiv2


class ChaosHandler():
    """Files handler."""

    def file(self, path):
        """Detect file type and handle it."""
        mimetype, encoding = mimetypes.guess_type(path)

        logging.info('MimeType: %s' % (
            mimetype if mimetype else 'unknown'
        ))

        if mimetype in config.types['images']:
            self.image(path)

    def image(self, path):
        """Handle image files."""
        logging.info('Processing image %s' % path)

        exif = GExiv2.Metadata(path)

        created_at = exif.get_date_time()

        move_to = os.path.join(
            config.paths['order'],
            '%04d' % created_at.year,
            '%02d' % created_at.month,
            '%02d' % created_at.day,
        )
        logging.info('Moving image to %s' % move_to)

        if not os.path.exists(move_to):
            logging.info(""" Destination path doesn\'t exists... \
Making directory...""")
            os.makedirs(move_to)

        destination = os.path.join(move_to, os.path.basename(path))

        i = 1
        while os.path.exists(destination):
            filename, extension = os.path.basename(path).split('.')
            destination = os.path.join(
                move_to,
                os.path.basename(
                    ".".join([
                        "%s_%03d" % (filename, i),
                        extension
                    ])
                )
            )
            i += 1

        logging.info('%s \t => \t %s' % (path, destination))
        shutil.move(path, destination)
