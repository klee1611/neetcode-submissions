class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # [-2, -1, -1, 0, 1, 2, 3, 4]
        targets = []
        for n in nums:
            targets.append(-n) # [2, 1, 1, 0, -1, -2, -3, -4]

        nums_len = len(nums)
        r = []
        for i in range(nums_len):
            for j in range(i+1, nums_len):
                if nums[j] > targets[i]:
                    break
                target = targets[i] - nums[j]
                left, right = j+1, nums_len
                while left < right:
                    mid = (left + right) // 2
                    if nums[mid] == target:
                        if [nums[i], nums[j], nums[mid]] not in r:
                            r.append([nums[i], nums[j], nums[mid]])
                        break
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid
        return r