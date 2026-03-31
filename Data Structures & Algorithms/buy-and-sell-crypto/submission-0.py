class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        cur_low, cur_profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] - cur_low > cur_profit:
                cur_profit = prices[i] - cur_low
            if prices[i] < cur_low:
                cur_low = prices[i]

        return cur_profit
            