from ubuntu_security import UbuntuRelease


def test_init():
    r = UbuntuRelease(
        "Focal Fossa", "20.04", True, False, "https://1", "https://2", "https://3"
    )

    assert r.codename == "focal"
    assert r.full_name == "Focal Fossa"
    assert r.version == "20.04"
    assert r.is_lts is True
    assert r.is_devel is False
    assert r.esm_repo_url == "https://1"
    assert r.esm_apps_repo_url == "https://2"
    assert r.esm_infra_repo_url == "https://3"


def test_from_dict():
    d = {
        "full_name": "Bionic Beaver",
        "version": "18.04",
        "is_lts": True,
        "is_devel": True,
        "esm_repo_url": "https://1",
        "esm_apps_repo_url": "https://2",
        "esm_infra_repo_url": "https://3",
    }

    r = UbuntuRelease.from_dict(d)

    assert r.codename == "bionic"
    assert r.full_name == "Bionic Beaver"
    assert r.version == "18.04"
    assert r.is_lts is True
    assert r.is_devel is True
    assert r.esm_repo_url == "https://1"
    assert r.esm_apps_repo_url == "https://2"
    assert r.esm_infra_repo_url == "https://3"


def test_from_dict_is_lts_default():
    d = {"full_name": "Bionic Beaver", "version": "18.04"}
    r = UbuntuRelease.from_dict(d)

    assert r.is_lts is False


def test_from_dict_is_devel_default():
    d = {"full_name": "Bionic Beaver", "version": "18.04"}
    r = UbuntuRelease.from_dict(d)

    assert r.is_devel is False


def test_from_dict_esm_repo_urldefault():
    d = {"full_name": "Bionic Beaver", "version": "18.04"}
    r = UbuntuRelease.from_dict(d)

    assert r.esm_repo_url is None


def test_from_dict_esm_apps_repo_urldefault():
    d = {"full_name": "Bionic Beaver", "version": "18.04"}
    r = UbuntuRelease.from_dict(d)

    assert r.esm_apps_repo_url is None


def test_from_dict_esm_infra_repo_urldefault():
    d = {"full_name": "Bionic Beaver", "version": "18.04"}
    r = UbuntuRelease.from_dict(d)

    assert r.esm_infra_repo_url is None


def test_esm_available():
    d = {"full_name": "Bionic Beaver", "version": "18.04", "esm_repo_url": "https://1"}
    r = UbuntuRelease.from_dict(d)

    assert r.esm_available is True


def test_esm_apps_available():
    d = {
        "full_name": "Bionic Beaver",
        "version": "18.04",
        "esm_apps_repo_url": "https://1",
    }
    r = UbuntuRelease.from_dict(d)

    assert r.esm_apps_available is True


def test_esm_infra_available():
    d = {
        "full_name": "Bionic Beaver",
        "version": "18.04",
        "esm_infra_repo_url": "https://1",
    }
    r = UbuntuRelease.from_dict(d)

    assert r.esm_infra_available is True


def test_esm_not_available():
    d = {"full_name": "Bionic Beaver", "version": "18.04"}
    r = UbuntuRelease.from_dict(d)

    assert r.esm_available is False
    assert r.esm_apps_available is False
    assert r.esm_infra_available is False
