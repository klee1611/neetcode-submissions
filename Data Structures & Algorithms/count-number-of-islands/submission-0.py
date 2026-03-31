class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])

        def dfs(x, y, r):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return

            nonlocal count
            if not r:
                count += 1
            grid[x][y] = '0'
            dfs(x+1, y, True)
            dfs(x-1, y, True)
            dfs(x, y+1, True)
            dfs(x, y-1, True)

        for i in range(m):
            for j in range(n):
                dfs(i, j, False)

        return count