class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        return max(self.rob_helper(nums[:-1]), self.rob_helper(nums[1:]))

    def rob_helper(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        money = [0] * n
        money[0] = nums[0]
        money[1] = max(nums[0], nums[1])
        for i in range(2, n):
            money[i] = max(money[i-1], nums[i] + money[i-2])

        return money[-1]