import logging
from pythonjsonlogger import jsonlogger
from config import Config


# Basic logger config
def make_logger(level):
    log = logging.getLogger("flashcards-api")
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    logHandler.setFormatter(formatter)
    log.addHandler(logHandler)
    log.setLevel(level)
    return log


log = make_logger(Config.log_level)
