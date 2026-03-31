class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, len(nums)
        while l < r:
            print(l, r)
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r-1]:
                    l = mid + 1
                else:
                    r = mid
        return -1
                