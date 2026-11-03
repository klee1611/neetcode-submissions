class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        curMin, curMax, res = nums[0], nums[0], nums[0]
        for i in range(1, n):
            tmp = nums[i] * curMax
            curMax = max(nums[i], tmp, nums[i] * curMin)
            curMin = min(nums[i], tmp, nums[i] * curMin)
            res = max(res, curMax)

        return res