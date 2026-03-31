class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        store = self.store[key]
        if not store or store[0][0] > timestamp:
            return ""
        
        if timestamp > store[-1][0]:
            return store[-1][1]

        l, r = 0, len(store)
        res = store[0][1]
        while l < r:
            mid = (l + r) // 2
            if store[mid][0] <= timestamp:
                res = store[mid][1]
                l = mid + 1
            else:
                r = mid
        return res