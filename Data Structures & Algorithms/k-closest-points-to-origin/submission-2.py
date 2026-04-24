class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            d = x * x + y * y
            heapq.heappush(heap, (-d, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)

        return [ p for d, p in heap ]