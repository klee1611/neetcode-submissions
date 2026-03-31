class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        l = []
        for key, v in count.items():
            l.append([key, v])

        l.sort(key=lambda x: x[1])
        return [x[0] for x in l[-k:]]