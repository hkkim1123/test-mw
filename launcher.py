import logging.config

from logging_conf import LOGGING_CONFIG
from test import start


if __name__ == '__main__':
    logging.config.dictConfig(LOGGING_CONFIG)
    start()

