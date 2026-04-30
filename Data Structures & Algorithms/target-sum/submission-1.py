class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0

        def dfs(prev, idx):
            nonlocal count
            if idx == len(nums) - 1:
                if prev + nums[idx] == target:
                    count += 1
                if prev - nums[idx] == target:
                    count += 1
                return

            dfs(prev + nums[idx], idx + 1)
            dfs(prev - nums[idx], idx + 1)

        dfs(0, 0)

        return count