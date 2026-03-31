class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return -1 if nums[0] != target else 0

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            print(mid, nums[mid])
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r-1]:
                if nums[mid] < target and target <= nums[r-1]:
                    print('a', target, nums[mid], nums[r-1])
                    l = mid +1
                else:
                    print('b', target, nums[mid], nums[r-1])
                    r = mid
            else:
                if nums[l] <= target and target < nums[mid]:
                    print('c', target, nums[l], nums[mid])
                    r = mid
                else:
                    print('d', target, nums[mid], nums[r-1])
                    l = mid + 1
        return -1