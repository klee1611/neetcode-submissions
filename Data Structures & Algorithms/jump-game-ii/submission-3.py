class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        dp = [float('inf')] * n
        dp[-1] = 0
        for i in range(n-2, -1, -1):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= n:
                    break
                dp[i] = min(dp[i], dp[j]+1)

        return dp[0]