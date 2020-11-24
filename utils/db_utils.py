import logging

from utils import check_process_time
from utils.db_session import (
    db_session, DATABASE_NAME, STORE_CONFIG_TABLE
)


@check_process_time('tagModel')
@db_session
def get_tag_count_by_store(conn=None):
    pass


@db_session
def get_all_store_code(conn=None):
    return list(conn[DATABASE_NAME][STORE_CONFIG_TABLE].find({}, {'_id': False}))

