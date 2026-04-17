class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        row, col = len(grid), len(grid[0])
        directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        size = 0
        def cal(x, y):
            if not 0 <= x < row or not 0 <= y < col or grid[x][y] != 1:
                return

            nonlocal size
            size += 1
            grid[x][y] = -1
            for dx, dy in directs:
                cal(x + dx, y + dy)

            return

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    size = 0
                    cal(x, y)
                    res = max(res, size)
        
        return res