class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        r = []
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j <= k:
                while j > i+1 and nums[j] == nums[j-1] and j < k:
                    j += 1
                if j >= k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    r.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return r
                