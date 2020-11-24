import sys


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'complex': {
            'format': '%(asctime)s %(process)5.5s|%(threadName)10.10s|%(levelname)5.5s|'
                      '%(filename)20.20s:%(lineno)-3s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'screen': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'complex',
            'stream': sys.stdout,
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'INFO',
            'formatter': 'complex',
            'filename': '/var/log/uwsgi/test-mw.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 3,
            'encoding': 'utf8',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG',
    },
}
