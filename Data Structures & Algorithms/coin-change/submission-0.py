class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort()
        if coins[0] > amount:
            return -1

        dp = [float('inf') for _ in range(amount+1)]
        for i in range(amount+1):
            if i < coins[0]:
                dp[i] = 0
                continue
            for j in range(len(coins)):
                if coins[j] == i:
                    dp[i] = 1
                if coins[j] < i and dp[i - coins[j]]:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])

        return dp[amount] if dp[amount] < float('inf') else -1