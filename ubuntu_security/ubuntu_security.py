import logging

from ust_download_cache import USTDownloadCache

from .service_locator import ubuntu_security_service_locator


def get_null_logger():
    if get_null_logger._null_logger is None:
        get_null_logger._null_logger = logging.getLogger("ubuntu_security_null")
        get_null_logger._null_logger.addHandler(logging.NullHandler())

    return get_null_logger._null_logger


get_null_logger._null_logger = None


def initialize(user_specified_logger=None):
    if user_specified_logger is None:
        ubuntu_security_service_locator.logger = get_null_logger()
    else:
        ubuntu_security_service_locator.logger = user_specified_logger

    ubuntu_security_service_locator.download_cache = USTDownloadCache(
        ubuntu_security_service_locator.logger
    )
