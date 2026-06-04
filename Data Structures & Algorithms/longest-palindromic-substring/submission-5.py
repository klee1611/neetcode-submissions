class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_len, res = 1, s[0]
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, n):
                if s[i] != s[j]:
                    continue
                
                if j != i + 1:
                    if dp[i+1][j-1]:
                        dp[i][j] = True
                else:
                    dp[i][j] = True

                if dp[i][j]:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        res = s[i:j+1]

        return res