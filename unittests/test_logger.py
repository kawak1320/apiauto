"""
(c) Copyright Jalasoft. 2023

logger.py
    configuration of logger file
"""

import logging
import unittest

from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.DEBUG)


class TestLogger(unittest.TestCase):
    """
    Configure logging instance
    :param
    :return:
    """
    def test_logger(self):
        """
            Configure logging instance
            :param
            :return:
            """
        LOGGER.debug("log DEBUG level")
        LOGGER.info("log INFO level")
        LOGGER.warning("log WARNING level")
        LOGGER.error("log ERROR level")
        LOGGER.critical("log CRITICAL level")
