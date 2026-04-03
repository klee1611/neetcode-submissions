class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return sum(nums)

        r = nums[0]
        larg_sum_arr = [nums[0]] * n
        for i in range(1, n):
            larg_sum_arr[i] = max(nums[i] + larg_sum_arr[i-1], nums[i])
            r = max(r, larg_sum_arr[i])

        return r