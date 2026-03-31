class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n_count = defaultdict(int)
        for n in nums:
            n_count[n] += 1

        nums.sort()
        r = []
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue

            n_count[nums[i]] -= 1
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[j] > -nums[i]:
                    break
                
                n_count[nums[j]] -= 1
                t = -nums[i] - nums[j]
                if t < nums[j]:
                    n_count[nums[j]] += 1
                    continue
                if n_count[t] > 0:
                    r.append([nums[i], nums[j], t])
                n_count[nums[j]] += 1
            n_count[nums[i]] += 1

        return r