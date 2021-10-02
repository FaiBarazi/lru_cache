from collections import OrderedDict


class LRUCache:
    def __init__(self, max_capacity=1):
        if max_capacity == 0:
            raise ValueError(
                'Cannot instantiate LRUCache with 0 capacity'
                )
        self.cache = OrderedDict()
        self.capacity = max_capacity

    def get(self, key):
        value = self.cache.get(key)
        if not value:
            return
        else:
            self.cache.move_to_end(key)
        return value

    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def delete(self, key):
        self.cache.pop(key, None)

    def reset(self):
        self.cache = OrderedDict()

    def __len__(self):
        return len(self.cache)
