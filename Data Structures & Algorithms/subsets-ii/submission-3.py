class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(idx, subset):
            print(idx, subset)
            if idx == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            backtrack(idx + 1, subset)

        backtrack(0, [])
        return res