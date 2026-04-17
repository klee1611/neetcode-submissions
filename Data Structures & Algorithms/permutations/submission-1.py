class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            for subpermute in self.permute(nums[1:]):
                res.append([nums[0]] + subpermute)
            nums[0], nums[i] = nums[i], nums[0]
        return res