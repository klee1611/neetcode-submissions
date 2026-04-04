class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        max_len, res = 1, s[0]
        for i in range(n-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, n):
                dp[i][j] = True if s[i] == s[j] and (dp[i+1][j-1] or j == i + 1) else False
                if dp[i][j]:
                    str_len = j - i + 1
                    if str_len > max_len:
                        max_len = str_len
                        res = s[i:j+1]

        return res