class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, n in enumerate(nums):
            table[n] = i

        for i in range(len(nums)):
            if table.get(target-nums[i], -1) > i:
                return [i, table[target-nums[i]]]