class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if i and n == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                result = n + nums[l] + nums[r]
                if result == 0:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif result < 0:
                    l += 1
                else:
                    r -= 1

        return res