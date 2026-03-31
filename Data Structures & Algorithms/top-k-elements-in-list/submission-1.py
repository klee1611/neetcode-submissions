class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}
        for n in nums:
            if n in freq_count:
                freq_count[n] = freq_count[n] + 1
            else:
                freq_count[n] = 1
        freq_list = [ [x, y] for x, y in freq_count.items() ]
        r = sorted(freq_list, key=lambda x: x[1], reverse = True)[:k]
        return [x[0] for x in r]