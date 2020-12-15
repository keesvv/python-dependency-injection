import redis

class RedisStorageProvider:
    def __init__(self):
        self.client = redis.Redis(host="localhost", port=6379)

    def read(self, object_id):
        return self.client.get(object_id).decode("utf-8")

    def write(self, object_id, content):
        self.client.set(object_id, content)
