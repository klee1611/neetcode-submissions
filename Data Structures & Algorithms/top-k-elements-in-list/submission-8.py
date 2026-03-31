class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        freq = [[] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            while freq[i] != []:
                res.append(freq[i].pop())
            if len(res) == k:
                break
        return res