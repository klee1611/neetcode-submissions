class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not self.data[key] or self.data[key][0][1] > timestamp:
            return ""
        
        data = self.data[key]
        res = ""
        l, r = 0, len(data)
        while l < r:
            mid = (l + r) // 2
            if data[mid][1] <= timestamp:
                if res:
                    res = min(res, (timestamp - data[mid][1], data[mid][0]))
                else:
                    res = (timestamp - data[mid][1], data[mid][0])
            if data[mid][1] > timestamp:
                r = mid
            else:
                l = mid + 1
        return res[1]