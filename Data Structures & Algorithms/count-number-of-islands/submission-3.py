class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        row, col = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] != "1":
                return

            grid[x][y] = "0"
            for dx, dy in directs:
                dfs(x+dx, y+dy)

        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1":
                    count += 1
                    dfs(x, y)

        return count