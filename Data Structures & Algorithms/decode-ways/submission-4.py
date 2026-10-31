class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        dp[-1] = 1 if s[-1] != "0" else 0

        for i in range(n-2, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue

            dp[i] = dp[i+1]

            if s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2] if i < n-2 else 1

        return dp[0]