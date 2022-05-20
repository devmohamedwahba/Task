"""
    Logger Module
"""
import logging.config
import logging

config = {
   "version": 1,
   "disable_existing_loggers": True,
   "formatters": {
       "standard": {
           "format": "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
           "datefmt": "%d-%m-%Y %H:%M:%S",
       },
       "json": {
        "format": "%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
        "datefmt": "%d-%m-%Y %H:%M:%S",
        "class": "pythonjsonlogger.jsonlogger.JsonFormatter"
    }
   },
   "handlers": {
       "standard": {
           "class": "logging.StreamHandler",
           "formatter": "json"
       }
   },
   "loggers": {
       "": {
           "handlers": ["standard"],
           "level": logging.INFO
       }
   }
}

logging.config.dictConfig(config)
Logger = logging.getLogger(__name__)
