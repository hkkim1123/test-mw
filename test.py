import logging
import time
from queue import Queue
from threading import Thread

from utils.db_session import create_mongo_client


queue = Queue()




def notification_executor():
    logging.info("notification_recv method start")
    while True:
        try:
            message = queue.get()
            if message == "product update":  # product update
                logging.info("message : %s", message)
            elif message == "template update":  # template update
                logging.info("message : %s", message)
            else:
                logging.info("message : %s", message)
        except Exception as e:
            logging.exception("handle error : %s", e)


def notification_recv():
    logging.info("notification_check method start")
    count = 0
    while True:
        try:
            # NotificationService signalR connect
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

    create_mongo_client()
    Thread(target=notification_executor).start()
    notification_recv()
    logging.info("start method end")

