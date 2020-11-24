import logging
import time
from queue import Queue
from threading import Thread
from utils.db_session import create_mongo_client
from scheduled_job import init_scheduled_job


queue = Queue()


def notification_executor():
    while True:
        try:
            message = queue.get()
            if message == "product update":  # product update
                logging.info("message : %s", message)
                # product update 처리
                # ....
            elif message == "template update":  # template update
                logging.info("message : %s", message)
                # template update 처리
                # ....
            else:
                logging.info("message : %s", message)
        except Exception as e:
            logging.exception("handle error : %s", e)


def notification_recv():
    logging.info(queue.maxsize())
    count = 0
    while True:
        try:
            # NotificationService signalR connect
            # NotificationService message recv
            # .....

            # queue test
            if count % 2 == 0:
                queue.put("product update")
            else:
                queue.put("template update")
            time.sleep(50)
            count += 1
            pass
        except Exception as e:
            logging.exception("handle error : %s", e)


def start():
    logging.info("init start method")
    create_mongo_client()  # mongo connect
    init_scheduled_job()  # cron
    Thread(target=notification_executor).start()  # NotificationService message executor
    notification_recv()  # NotificationService message receive

