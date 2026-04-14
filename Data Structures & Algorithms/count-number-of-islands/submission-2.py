class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = len(grid), len(grid[0])

        def dfs(x, y):
            if 0 > x or x >= row or 0 > y or y >= col or \
                grid[x][y] != "1":
                return

            grid[x][y] = "0"
            for dx, dy in directs:
                dfs(x + dx, y + dy)

            return

        for x in range(row):
            for y in range(col):
                if grid[x][y] == "1":
                    count += 1
                    dfs(x, y)

        return count