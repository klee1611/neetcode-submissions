class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            print(l, r, mid)
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r-1]:
                    l = mid + 1
                else:
                    r = mid
        return -1