class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, area = 0, 0
        row, col = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == 0:
                return

            nonlocal area
            area += 1
            grid[x][y] = 0
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x-1, y,)
            dfs(x+1, y)


        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    max_area = max(max_area, area)
        return max_area