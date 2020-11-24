import logging
from functools import wraps
from pymongo import MongoClient
from config import DATABASE_URI

DATABASE_NAME = 'infortab'
STORE_CONFIG_TABLE = 'store_config'

client = None


def create_mongo_client():
    global client
    client = db_connect()


def db_connect():
    logging.info('New db connection is established.')
    return MongoClient(DATABASE_URI)


def db_session(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        global client
        return func(*args, conn=client, **kwargs)

    return decorator

