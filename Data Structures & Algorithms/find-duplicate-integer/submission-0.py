class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            if not count[n]:
                count[n] += 1
            else:
                return n