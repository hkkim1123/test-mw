import time
import logging
from functools import wraps


def check_process_time(tag_name=''):
    def wrap(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            start_time = time.time()
            resp = func(*args, **kwargs)
            process_time = time.time() - start_time
            if process_time > 1:
                logging.warning('func : %s.%s(), process time : %s', tag_name, func.__name__, '%.6f' % process_time)
            else:
                logging.debug('func : %s.%s(), process time : %s', tag_name, func.__name__, '%.6f' % process_time)
            return resp
        return decorator
    return wrap

