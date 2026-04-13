class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i, n in enumerate(nums):
            if i and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] + n == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                if nums[l] + nums[r] + n < 0:
                    l += 1
                if nums[l] + nums[r] + n > 0:
                    r -= 1
        return res