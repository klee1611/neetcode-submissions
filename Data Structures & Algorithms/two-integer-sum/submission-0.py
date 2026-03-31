class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain = {}
        for i in range(len(nums)):
            if nums[i] in remain:
                return [remain.get(nums[i]), i]
            remain[target-nums[i]] = i