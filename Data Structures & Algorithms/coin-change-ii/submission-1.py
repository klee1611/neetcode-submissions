class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        combination = [0] * (amount + 1)

        coins.sort()
        for coin in coins:
            for i in range(amount + 1):
                if i < coin:
                    continue

                if i == coin:
                    combination[i] += 1
                    continue

                combination[i] += combination[i - coin]

        return combination[-1]