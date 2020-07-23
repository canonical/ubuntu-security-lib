def _raise_on_uninitialized(attribute_name, attribute):
    if attribute is None:
        raise AttributeError(
            '%s has not been initialized. Try initializing the Ubuntu Security Library with "ubuntu_security.initialize()".'
            % attribute_name
        )


def _raise_on_already_initialized(attribute_name, attribute):
    if attribute is not None:
        raise AttributeError("%s has already been initialized." % attribute_name)


class ServiceLocator:
    def __init__(self):
        self._logger = None
        self._download_cache = None

    @property
    def logger(self):
        _raise_on_uninitialized("logger", self._logger)

        return self._logger

    @logger.setter
    def logger(self, logger):
        _raise_on_already_initialized("logger", self._logger)

        self._logger = logger

    @property
    def download_cache(self):
        _raise_on_uninitialized("download_cache", self._download_cache)

        return self._download_cache

    @download_cache.setter
    def download_cache(self, download_cache):
        _raise_on_already_initialized("download_cache", self._download_cache)

        self._download_cache = download_cache


ubuntu_security_service_locator = ServiceLocator()
