import pytest

from ubuntu_security.service_locator import ServiceLocator


def test_uninitialized_logger():
    sl = ServiceLocator()
    with pytest.raises(AttributeError) as ae:
        sl.logger.debug("test")

    assert "logger has not been initialized" in str(ae)


def test_reinitialize_logger():
    sl = ServiceLocator()
    sl.logger = "test1"

    with pytest.raises(AttributeError) as ae:
        sl.logger = "test2"

    assert "logger has already been initialized" in str(ae)


def test_get_logger():
    test_list = ["a", "b"]
    sl = ServiceLocator()
    sl.logger = test_list

    assert sl.logger is test_list


def test_uninitialized_download_cache():
    sl = ServiceLocator()
    with pytest.raises(AttributeError) as ae:
        sl.download_cache.get_data_from_url()

    assert "download_cache has not been initialized" in str(ae)


def test_reinitialize_download_cache():
    sl = ServiceLocator()
    sl.download_cache = "test1"

    with pytest.raises(AttributeError) as ae:
        sl.download_cache = "test2"

    assert "download_cache has already been initialized" in str(ae)


def test_get_download_cache():
    test_list = ["a", "b"]
    sl = ServiceLocator()
    sl.download_cache = test_list

    assert sl.download_cache is test_list
