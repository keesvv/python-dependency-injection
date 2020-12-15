import sys
from os import path, makedirs
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide

class StorageProvider:
    def read(self, object_id):
        pass

    def write(self, object_id, content):
        pass

class FSStorageProvider(StorageProvider):
    def __init__(self):
        self.storage_dir = "./fs-storage"

    def get_path(self, object_id):
        return path.abspath(
            path.join(self.storage_dir, object_id)
        )
    
    def create_dirs(self, object_path):
        object_parent = path.dirname(object_path)
        makedirs(object_parent, exist_ok=True)

    def read(self, object_id):
        object_path = self.get_path(object_id)

        try:
            f = open(object_path)
            content = f.read()
            f.close()
            return content
        except FileNotFoundError:
            return None

    def write(self, object_id, content):
        object_path = self.get_path(object_id)
        self.create_dirs(object_path)

        f = open(object_path, "w")
        f.write(content)
        f.close()

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
