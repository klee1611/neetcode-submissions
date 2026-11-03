class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return [nums]

        res = []
        def helper(idx):
            if idx == n-1:
                res.append(nums[:])
                return

            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                helper(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        helper(0)
        return res