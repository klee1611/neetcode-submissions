class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1

        for n in nums:
            min_num, max_num = cur_min * n, cur_max * n
            cur_min = min(n, min_num, max_num)
            cur_max = max(n, min_num, max_num)
            res = max(res, cur_max)

        return res