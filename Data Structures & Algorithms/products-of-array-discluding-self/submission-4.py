class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if 1 == len(nums):
            return nums[0]
        if 2 == len(nums):
            return [nums[1], nums[0]]

        pref = [nums[0] for n in nums]
        suff = [nums[-1] for n in nums]
        for i in range(len(nums)):
            if i > 0:
                pref[i] = pref[i-1] * nums[i]
            if i > 1:
                suff[-i] = suff[-(i-1)] * nums[-i]
        suff[0] = suff[1] * nums[0]
        print(pref, suff)

        r = [suff[1]]
        for i in range(1, len(nums)-1):
            r.append(pref[i-1] * suff[i+1])
        r.append(pref[-2])
        print(r)

        return r