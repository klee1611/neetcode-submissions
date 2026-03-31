class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        heap = []
        for key, v in count.items():
            heapq.heappush(heap, [-v, key])

        return [heapq.heappop(heap)[1] for x in range(k)]