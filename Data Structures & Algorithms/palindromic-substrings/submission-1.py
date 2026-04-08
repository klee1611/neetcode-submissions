class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = []
        for i in range(n):
            dp.append([0] * n)

        count = 0
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            count += 1
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    dp[i][j] = False
                    continue
                if j == i + 1:
                    dp[i][j] = True
                    count += 1
                    continue
                dp[i][j] = dp[i+1][j-1]
                if dp[i][j]:
                    count += 1
        return count