# log.py

import logging
import time
from logging.handlers import TimedRotatingFileHandler
from KommatiParaClients.config_reader import get_config

config = get_config()


def create_log(path: str):
    """
    This function creates log and covers rotation setup
    """
    logger = logging.getLogger('ApplicationLog')
    logger.setLevel(logging.INFO)
    format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = TimedRotatingFileHandler(
        path,
        when="m",
        interval=1,
        backupCount=3
        )
    file_handler.setFormatter(format)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(format)
    logger.addHandler(console_handler)


def log_init():
    log_file = "application.log"
    create_log(log_file)
    return logging.getLogger('ApplicationLog')
