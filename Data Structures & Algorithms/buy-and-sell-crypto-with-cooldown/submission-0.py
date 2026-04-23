class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        hold = float("-inf")
        rest = 0
        sold = 0

        for i in range(len(prices)):
            prev_sold = sold

            sold = hold + prices[i]
            hold = max(hold, rest - prices[i])
            rest = max(rest, prev_sold)

        return max(rest, sold)