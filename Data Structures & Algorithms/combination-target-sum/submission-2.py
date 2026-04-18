class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target <= 0:
            return []

        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n == target:
                res.append([n])
            if n > target:
                break
            if target - n < n:
                continue
            for sub_sum in self.combinationSum(nums[i:], target - n):
                res.append([n] + sub_sum)

        return res
