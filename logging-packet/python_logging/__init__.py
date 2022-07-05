
from os import path, remove
import logging
import logging.config
import json

if path.isfile('python_logging.log'):
    remove('python_logging.log')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# logger_handler = logging.FileHandler('python_logging.log')
# logger_handler.setLevel(logging.INFO)
#
# logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#
# logger_handler.setFormatter(logger_formatter)
#
# logger.addHandler(logger_handler)
# logger.info('Настройка логгирования окончена!')

with open('python_logging/logcnf.json', 'r') as logCnf:
    config_dict = json.load(logCnf)

logging.config.dictConfig(config_dict)

logger = logging.getLogger(__name__)
logger.info('Настройка логгирования окончена!')
