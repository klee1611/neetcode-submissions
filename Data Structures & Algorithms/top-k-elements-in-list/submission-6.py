class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res