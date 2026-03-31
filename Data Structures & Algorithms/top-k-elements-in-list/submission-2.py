class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}
        for n in nums:
            freq_count[n] = freq_count.get(n, 0) + 1

        freq = [[] for x in range(len(nums)+1)]
        for x, y in freq_count.items():
            freq[y].append(x)

        r = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                r.append(n)
            if len(r) == k:
                return r