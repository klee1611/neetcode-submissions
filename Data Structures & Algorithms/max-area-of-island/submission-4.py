class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        area, max_area = 0, 0
        def dfs(x, y):
            if x < 0 or y < 0 or x >= row or y >= col \
                or grid[x][y] != 1:
                return
            
            nonlocal area
            area += 1
            grid[x][y] = -1
            for dx, dy in dirs:
                dfs(x+dx, y+dy)

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    area = 0
                    dfs(x, y)
                    max_area = max(max_area, area)

        return max_area