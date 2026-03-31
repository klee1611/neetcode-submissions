class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])

        def update(x, y, step):
            if x < 0 or x >= row or y < 0 or y >= col or step > grid[x][y]:
                return

            grid[x][y] = step
            step += 1
            update(x-1, y, step)
            update(x+1, y, step)
            update(x, y-1, step)
            update(x, y+1, step)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    update(i, j, 0)