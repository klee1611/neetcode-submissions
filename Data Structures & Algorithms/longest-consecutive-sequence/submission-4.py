class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        print(nums)
        l = []
        cur = 1
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1]+1:
                cur += 1
            else:
                l.append(cur)
                cur = 1
            print(i, nums[i], cur)
        l.append(cur)
        return max(l)