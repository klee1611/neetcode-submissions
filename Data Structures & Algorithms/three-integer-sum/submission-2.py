class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        r = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            count[nums[i]] -= 1
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                count[nums[j]] -= 1
                target = -nums[i]-nums[j]
                if target >= nums[j] and count[target] > 0:
                    r.append([nums[i], nums[j], target])
                count[nums[j]] += 1
            count[nums[i]] += 1
        return r