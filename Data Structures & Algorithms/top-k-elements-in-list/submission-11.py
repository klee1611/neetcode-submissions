class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        heap = []
        for n, c in count.items():
            heap.append((-c, n))
        heapq.heapify(heap)

        r = []
        for i in range(k):
            r.append(heapq.heappop(heap)[1])

        return r