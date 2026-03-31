class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)

        while l < r:
            if nums[l] < nums[r-1]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[r-1]:
                r = mid
            else:
                l = mid + 1
        return res