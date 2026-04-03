class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        def rob_line(houses):
            count = len(houses)
            money = [houses[0]] * count

            money[0] = houses[0]
            money[1] = max(houses[0], houses[1])
            max_money = money[1]
            for i in range(2, count):
                money[i] = max(houses[i] + money[i-2], money[i-1])
                max_money = max(max_money, money[i])

            return max_money

        return max(rob_line(nums[1:]), rob_line(nums[:-1]))