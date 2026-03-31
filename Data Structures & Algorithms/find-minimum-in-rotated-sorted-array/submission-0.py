class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]

        if nums[-1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums)
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[r-1]:
                l = mid + 1
            else:
                r = mid
        return nums[l]