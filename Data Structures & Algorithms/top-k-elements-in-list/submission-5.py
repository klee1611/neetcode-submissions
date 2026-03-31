class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        freq = [[] for i in range(len(nums)+1)]
        for c_k, c_v in count.items():
            freq[c_v].append(c_k)

        r = []
        for f in freq[::-1]:
            if f:
                for n in f:
                    r.append(n)
                    if len(r) == k:
                        return r