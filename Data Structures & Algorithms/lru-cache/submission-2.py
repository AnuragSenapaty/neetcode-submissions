class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.used = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.mp:
            self.used.remove(key)
            self.used.append(key)
            return self.mp[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key] = value
            self.used.remove(key)
            self.used.append(key)
        else:
            if len(self.mp) >= self.cap:
                lru = self.used.pop(0)
                del self.mp[lru]
            self.mp[key] = value
            self.used.append(key)