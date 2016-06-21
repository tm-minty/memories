import logging

DEBUG = True

debug_level = logging.ERROR
log_file = None

paths = {
    'chaos': '/tmp/memories/chaos',
    'order': '/tmp/memories/order',
}

types = {
    'images': [
        'image/gif',
        'image/jpeg',
        'image/pjpeg',
        'image/png',
        'image/svg+xml',
        'image/tiff',
        'image/vnd.microsoft.icon',
        'image/vnd.wap.wbmp',
    ],
}
