class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        exist = set(nums)

        res = 0
        for n in nums:
            cur_len = 1
            while n+1 in exist:
                cur_len += 1
                n += 1
            res = max(res, cur_len)

        return res