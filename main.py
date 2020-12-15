import sys
from storage_provider import StorageProvider, FSStorageProvider
from os import path, makedirs
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    storage_provider: StorageProvider = providers.Factory(FSStorageProvider)

@inject
def entry(
    storage_provider: StorageProvider = Provide[Container.storage_provider]
):
    storage_provider.write("hello/world", "Hello, world!")
    content = storage_provider.read("hello/world")
    print(content)

if __name__ == '__main__':
    container = Container()
    container.wire(modules=[sys.modules[__name__]])
    entry()
