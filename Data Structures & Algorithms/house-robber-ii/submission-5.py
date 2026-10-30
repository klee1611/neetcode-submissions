class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(val):
            n = len(val)
            if n == 1:
                return val[0]

            dp = [0] * n
            dp[0] = val[0]
            dp[1] = max(val[0], val[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], val[i] + dp[i-2])

            return dp[-1]

        return max(helper(nums[:-1]), helper(nums[1:]))