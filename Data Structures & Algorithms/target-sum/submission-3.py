class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [ collections.defaultdict(int) for _ in range(len(nums)) ]
        dp[0][nums[0]] += 1
        dp[0][-nums[0]] += 1

        for i in range(0, len(nums)-1):
            for total, count in dp[i].items():
                dp[i+1][total + nums[i+1]] += count
                dp[i+1][total - nums[i+1]] += count

        return dp[-1][target]