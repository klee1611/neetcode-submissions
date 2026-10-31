class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        if amount == 0:
            return 0
        if amount < coins[0]:
            return -1

        dp = [float('inf')] * (amount + 1)
        for i in range(coins[0], amount+1):
            for coin in coins:
                if coin > i:
                    break
                if coin == i:
                    dp[i] = 1
                    break
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[-1] if dp[-1] < float('inf') else -1