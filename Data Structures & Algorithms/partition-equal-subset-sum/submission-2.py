class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        if n == 2:
            return nums[0] == nums[1]

        sum_nums = sum(nums)
        if sum_nums % 2:
            return False
        target = sum_nums // 2

        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
            if nums[i] <= target:
                dp[i][nums[i]] = True

        for i in range(1, n):
            for j in range(target+1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i]]
            if dp[i][target]:
                return True

        return False