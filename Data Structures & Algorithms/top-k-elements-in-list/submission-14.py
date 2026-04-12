class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        min_heap = []
        for n, c in count.items():
            heapq.heappush(min_heap, (c, n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [ n for c, n in min_heap ]