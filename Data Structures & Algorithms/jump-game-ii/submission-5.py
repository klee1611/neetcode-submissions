class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                if i + nums[i] > farthest:
                    farthest = i + nums[i]
            l = r + 1
            r = farthest
            count += 1
        
        return count