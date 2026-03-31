class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        max_p = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > lowest:
                max_p = max(max_p, prices[i] - lowest)
            else:
                lowest = prices[i]
        return max_p