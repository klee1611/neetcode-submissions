class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        max_len, max_str = 0, s[0]

        for i in range(1, n):
            for j in range(n-i):
                start, end = j, j+i
                if s[start] != s[end]:
                    dp[start][end] = False
                    continue
                if start == end - 1:
                    dp[start][end] = True
                else:
                    dp[start][end] = dp[start+1][end-1]
                if dp[start][end] and i > max_len:
                    max_len, max_str = i, s[start:end+1]

        return max_str