from ubuntu_security import UbuntuRelease

from .service_locator import ubuntu_security_service_locator

UBUNTU_RELEASE_STATUS_URL = (
    "https://people.canonical.com/~ubuntu-security/"
    "ubuntu-security-lib/ubuntu-security-release-status.json"
)


def load_ubuntu_release_statuses():
    releases = {}
    uct_data = ubuntu_security_service_locator.download_cache.get_data_from_url(
        UBUNTU_RELEASE_STATUS_URL
    )

    for release, data in uct_data["releases"].items():
        releases[release] = UbuntuRelease.from_dict(data)

    return releases
