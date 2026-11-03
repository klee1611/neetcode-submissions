class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        res = 1
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)
                res = max(res, dp[i])
        return res