import logging
import os

logging.basicConfig(level=os.getenv('LOG_LEVEL') or 'INFO')
logger = logging.getLogger()
