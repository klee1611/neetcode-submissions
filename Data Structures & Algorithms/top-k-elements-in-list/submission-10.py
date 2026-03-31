class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = defaultdict(int)
        for n in nums:
            count_hash[n] += 1

        count = [[] for i in range(len(nums)+1)]
        for n, c in count_hash.items():
            count[c].append(n)

        res = []
        for i in range(len(count)-1, -1, -1):
            for n in count[i]:
                res.append(n)
            if len(res) == k:
                return res