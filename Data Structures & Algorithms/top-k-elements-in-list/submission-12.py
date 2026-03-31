class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        bucket = [[] for i in range(len(nums)+1)]
        for n, c in count.items():
            bucket[c].append(n)

        r = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                r += bucket[i]
            if len(r) == k:
                break
        return r