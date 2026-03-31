class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if 1 == len(nums):
            return nums[0]
        if 2 == len(nums):
            return [nums[1], nums[0]]

        pref = [1 for i in range(len(nums))]
        suff = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
                pref[i] = nums[i-1] * pref[i-1] 
        for i in range(len(nums)-2, -1, -1): 
                suff[i] = nums[i+1] * suff[i+1]
        print(pref, suff)

        return [ pref[i] * suff[i] for i in range(len(nums))]