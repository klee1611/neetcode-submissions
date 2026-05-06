class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.store[key]:
            return ""

        n = len(self.store[key])
        l, r = 0, n
        res = ""
        while l < r:
            mid = (l + r) // 2

            if self.store[key][mid][0] > timestamp:
                r = mid
            else:
                res = self.store[key][mid]
                l = mid + 1

        return res[1] if res != "" else ""