import json

import pytest

import ubuntu_security
from ubuntu_security import UbuntuRelease
from ubuntu_security.service_locator import ubuntu_security_service_locator


class MockDownloadCache:
    def __init__(self, file_name):
        with open(file_name) as f:
            self.data = json.load(f)

    def get_data_from_url(self, url):
        return self.data["data"]


@pytest.fixture(scope="module")
def ussl():
    ubuntu_security_service_locator.download_cache = MockDownloadCache(
        "tests/assets/ubuntu_releases.json"
    )
    yield
    ubuntu_security_service_locator._download_cache = None


def test_load_ubuntu_release_statuses(ussl):
    releases = ubuntu_security.load_ubuntu_release_statuses()

    assert len(releases.keys()) == 6
    assert "precise" in releases
    assert "trusty" in releases
    assert "xenial" in releases
    assert "bionic" in releases
    assert "focal" in releases
    assert "groovy" in releases

    for r in releases.values():
        assert isinstance(r, UbuntuRelease)
