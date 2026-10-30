class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        dp = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1

        for i in range(1, n):
            for j in range(n-i):
                start, end = j, j+i
                if s[start] != s[end]:
                    dp[start][end] = False
                    continue

                if start + 1 == end:
                    dp[start][end] = True
                else:
                    dp[start][end] = dp[start+1][end-1]

                if dp[start][end]:
                    count += 1

        return count