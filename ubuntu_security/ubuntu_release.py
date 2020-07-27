class UbuntuRelease:
    def __init__(
        self,
        full_name,
        version,
        is_lts,
        is_devel,
        esm_repo_url,
        esm_apps_repo_url,
        esm_infra_repo_url,
    ):
        self._codename = full_name.split(" ")[0].lower()
        self._full_name = full_name
        self._version = version
        self._is_lts = is_lts
        self._is_devel = is_devel
        self._esm_repo_url = esm_repo_url
        self._esm_apps_repo_url = esm_apps_repo_url
        self._esm_infra_repo_url = esm_infra_repo_url

    @property
    def codename(self):
        return self._codename

    @property
    def full_name(self):
        return self._full_name

    @property
    def version(self):
        return self._version

    @property
    def is_lts(self):
        return self._is_lts

    @property
    def is_devel(self):
        return self._is_devel

    @property
    def esm_repo_url(self):
        return self._esm_repo_url

    @property
    def esm_available(self):
        return self.esm_repo_url is not None

    @property
    def esm_apps_repo_url(self):
        return self._esm_apps_repo_url

    @property
    def esm_apps_available(self):
        return self.esm_apps_repo_url is not None

    @property
    def esm_infra_repo_url(self):
        return self._esm_infra_repo_url

    @property
    def esm_infra_available(self):
        return self.esm_infra_repo_url is not None

    @classmethod
    def from_dict(cls, ubuntu_release):
        return cls(
            ubuntu_release["full_name"],
            ubuntu_release["version"],
            ubuntu_release.get("is_lts", False),
            ubuntu_release.get("is_devel", False),
            ubuntu_release.get("esm_repo_url", None),
            ubuntu_release.get("esm_apps_repo_url", None),
            ubuntu_release.get("esm_infra_repo_url", None),
        )
