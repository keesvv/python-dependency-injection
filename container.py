from dependency_injector import containers, providers
from storage_provider import StorageProvider, FSStorageProvider, RedisStorageProvider

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    storage_provider: StorageProvider = providers.Factory(RedisStorageProvider)
