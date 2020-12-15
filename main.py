import sys
from container import Container
from storage_provider import StorageProvider
from dependency_injector.wiring import inject, Provide

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
