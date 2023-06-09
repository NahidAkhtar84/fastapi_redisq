import logging
from logging.config import dictConfig

from pydantic import BaseModel


class LogConfig(BaseModel):
    LOGGER_NAME: str = "ats"
    LOG_FORMAT: str = "%(levelprefix)s | %(pathname)s | %(lineno)d | %(levelname)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "ats": {"handlers": ["default"], "level": LOG_LEVEL},
    }


def log_config():
    dictConfig(LogConfig().dict())
    logger = logging.getLogger("fastapi_redisq")

    return logger


logger = log_config()

# Log Messages types
# info
# warning
# error
# debug
# critical
