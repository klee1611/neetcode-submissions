class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[-1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums)
        res = nums[0]
        while l < r:
            if nums[l] < nums[r-1]:
                return min(res, nums[l])

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        return res