class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 1:
            return [[s]]

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(1, n):
            for j in range(n-i):
                if s[j] != s[j+i]:
                    continue
                if i == 1:
                    dp[j][j+i] = True
                    continue
                dp[j][j+i] = dp[j+1][j+i-1]
        print(dp)

        res = []
        def dfs(idx, cur):
            if idx == n:
                res.append(cur[:])
                return

            for i in range(idx, n):
                if dp[idx][i]:
                    cur.append(s[idx:i+1])
                    dfs(i+1, cur)
                    cur.pop()
        dfs(0, [])
        return res