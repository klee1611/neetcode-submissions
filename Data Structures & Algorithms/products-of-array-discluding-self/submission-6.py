class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [1 for n in nums]
        suff = [1 for n in nums]

        for i in range(1, len(nums)):
            prev[i] = prev[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        print(prev, suff)

        return [prev[i] * suff[i] for i in range(len(nums))]