import logging

import pytest

import ubuntu_security
from ubuntu_security.service_locator import ubuntu_security_service_locator


@pytest.fixture()
def teardown_service_locator():
    yield
    ubuntu_security_service_locator._logger = None
    ubuntu_security_service_locator._download_cache = None


def test_not_none(teardown_service_locator):
    ubuntu_security.initialize()

    assert ubuntu_security_service_locator.logger is not None
    assert ubuntu_security_service_locator.download_cache is not None


def test_user_defined_logger(teardown_service_locator):
    test_logger = logging.getLogger("test_logger")
    ubuntu_security.initialize(test_logger)

    assert ubuntu_security_service_locator.logger is test_logger
