from os import path, makedirs
from . import StorageProvider

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
