class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_prof = prices[0], 0
        
        for price in prices:
            max_prof = max(max_prof, price - min_price)
            min_price = min(min_price, price)

        return max_prof