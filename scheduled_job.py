import logging
from utils.db_utils import (
    get_all_store_code, get_tag_count_by_store
)
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


@scheduler.scheduled_job('cron', hour='9')
def license_refresh():
    logging.info("scheduled_job license_refresh")
    store_code_list = get_all_store_code()
    # logging.info("store_code_list: {}".format(store_code_list))
    # ESL Controller에 tag count 받아오기
    # PRESTIGEService에 tagCount/storeId 넘기기


@scheduler.scheduled_job('cron', hour='9')
def update_branch_guid():
    logging.info("scheduled_job update_branch_guid")
    # ESL Controller에 StoreId 받기
    # PRESTIGEService에 StoreGuid 전달
    # PRESTIGEService가 StoreGuid전달
    # StoreGuid 저장(24시간동안?)


def init_scheduled_job():
    logging.info("init_scheduled_job start")
    scheduler.start()  # License refresh(daily), update BranchGuid(daily)

