class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        r = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                if j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue

                if nums[i] + nums[j] + nums[k] == 0:
                    r.append([nums[i], nums[j], nums[k]])
                    j, k = j+1, k-1
                    continue

                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    continue

                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1

        return r