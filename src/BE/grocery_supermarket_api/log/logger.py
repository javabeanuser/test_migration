import logging
import inspect
from config import Config
from logging.handlers import RotatingFileHandler

class Logger:

    logging.basicConfig(
        level=logging.getLevelName(Config.get_log_level()),
        format=Config.get_log_format(),
        datefmt=Config.get_log_datefmt(),
        handlers=[
            RotatingFileHandler(filename=Config.get_log_file(),
                                maxBytes=Config.get_log_max_bytes(),
                                backupCount=Config.get_log_backup_count()),
            logging.StreamHandler()
        ]
    )

    @staticmethod
    def info(message,  *args, **kwargs):
        logging.info(f"[{inspect.getmodule(inspect.stack()[1][0]).__name__}] {message}", *args, **kwargs)

    @staticmethod
    def debug(message, *args, **kwargs):
        logging.debug(f"[{inspect.getmodule(inspect.stack()[1][0]).__name__}] {message}", *args, **kwargs)

    @staticmethod
    def warn(message, *args, **kwargs):
        logging.warning(f"[{inspect.getmodule(inspect.stack()[1][0]).__name__}] {message}", *args, **kwargs)

    @staticmethod
    def error(message, *args, **kwargs):
        logging.error(f"[{inspect.getmodule(inspect.stack()[1][0]).__name__}] {message}", *args, **kwargs)

    @staticmethod
    def critical(message, *args, **kwargs):
        logging.critical(f"[{inspect.getmodule(inspect.stack()[1][0]).__name__}] {message}", *args, **kwargs)
