class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        l, r = 0, len(nums)
        res = nums[0]
        while l < r:
            mid = l + (r - l) // 2
            if nums[l] < nums[mid]:
                res = min(nums[l], res)
                l = mid+1
            else:
                res = min(res, nums[mid])
                r = mid

        return res