import logging
import time
from queue import Queue
from threading import Thread

from utils.db_session import create_mongo_client
from apscheduler.schedulers.background import BackgroundScheduler


queue = Queue()
scheduler = BackgroundScheduler()


@scheduler.scheduled_job('cron', minute='*/1')
def schedule_test():
    logging.info("schedule_test")


def notification_executor():
    logging.info("notification_executor method start")
    while True:
        try:
            message = queue.get()
            if message == "product update":  # product update
                logging.info("message : %s", message)
                # product update 처리
            elif message == "template update":  # template update
                logging.info("message : %s", message)
                # template update 처리
            else:
                logging.info("message : %s", message)
        except Exception as e:
            logging.exception("handle error : %s", e)


def notification_recv():
    logging.info("notification_recv method start")
    count = 0
    while True:
        try:
            # NotificationService signalR connect
            # NotificationService message recv

            # queue test
            if count % 2 == 0:
                queue.put("product update")
            else:
                queue.put("template update")
            time.sleep(3)
            count += 1
        except Exception as e:
            logging.exception("handle error : %s", e)


def start():
    logging.info("start method start")
    # ESL Controller 연동 api method
    # 1. 상품 바코드 스캔
    # - ESL Controller(barcode) -> comm-mw(barcode -> articleNumber) -> PRESITIGE(articleNumber) -> comm-mw(articleNumber -> barcode) -> ESL Controller(barcode)
    # 2. 태그 스캔

    scheduler.start()

    create_mongo_client()  # mongo connect
    Thread(target=notification_executor).start()  # NotificationService message executor
    notification_recv()  # NotificationService message receive

