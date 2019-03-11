import os
import logging
from logging.handlers import TimedRotatingFileHandler
from utils.config import LOG_PATH

class logger():
    def __init__(self,logger_name="framework"):
        self.logger = logging