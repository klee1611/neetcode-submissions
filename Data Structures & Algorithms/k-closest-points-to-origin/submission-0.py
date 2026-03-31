class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hash_map = defaultdict(list)
        for p in points:
            distance = p[0] ** 2 + p[1] ** 2
            hash_map[distance].append(p)

        heap = []
        for distance, points in hash_map.items():
            heapq.heappush(heap, (distance, points))

        res = []
        while len(res) < k:
            res += heapq.heappop(heap)[1]

        return res