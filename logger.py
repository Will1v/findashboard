import logging
from logging.handlers import RotatingFileHandler
import sys
import os
from datetime import datetime

DEFAULT_LOG_DIR = "/var/log/{}".format(os.getlogin())
DEFAULT_LOG_LEVEL = logging.INFO

def get_logger(logger_name, filename_prefix):
    print("get_logger for logger_name = {} and filename_prefix = {}".format(logger_name, filename_prefix))
    logger = logging.getLogger(logger_name)
    logger.setLevel(DEFAULT_LOG_LEVEL)

    if not os.path.exists(DEFAULT_LOG_DIR):
        print("Path {} does not exist, will try to create it...".format(DEFAULT_LOG_DIR))
        os.mkdir(DEFAULT_LOG_DIR)
    filepath = "{}/{}_{}.log".format(DEFAULT_LOG_DIR, filename_prefix, datetime.now().strftime('%Y%m%d_%H%M'))
    # if logger_name == filename_prefix and os.path.isfile(filepath):
    #     print("Logfile for {} already existing, will try to delete it...".format(logger_name))
    #     os.remove(filepath)
    #     print("Logfile for {} deleted".format(logger_name))

    handler = RotatingFileHandler(filepath, 'a', maxBytes=10000000, backupCount=1000)
    handler.setLevel(DEFAULT_LOG_LEVEL)
    formatter = logging.Formatter('%(asctime)s [%(name)s][%(levelname)s] %(message)s (%(pathname)s:%(lineno)s)')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    std_out_handler = logging.StreamHandler(sys.stdout)
    std_out_handler.setLevel(DEFAULT_LOG_LEVEL)
    std_out_handler.setFormatter(formatter)
    logger.addHandler(std_out_handler)

    logger.debug('Logger {} initiated'.format(logger_name))

    return logger

