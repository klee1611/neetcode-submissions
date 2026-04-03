class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        money = [nums[0]] * n # money[i] stands for the max money if i-th item is taken
        money[1] = nums[1]
        money[2] = nums[2] + nums[0]
        r = max(money[1], money[2])

        for i in range(3, n):
            money[i] = nums[i] + max(money[i-2], money[i-3])
            r = max(r, money[i])

        return r