class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1 if s[0] != "0" else 0

        dp = []
        for i in range(n):
            dp.append([0] * n)

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                for j in range(i, n):
                    dp[i][j] = 0
                continue
            dp[i][i] = 1
            for j in range(i+1, n):
                dp[i][j] = dp[i+1][j]
                if 0 < int(s[i:i+2]) < 27:
                    if j == i+1:
                        dp[i][j] += 1
                    else:
                        dp[i][j] += dp[i+2][j]
            
        return dp[0][n-1]