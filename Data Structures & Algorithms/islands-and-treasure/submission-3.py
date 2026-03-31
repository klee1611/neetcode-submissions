class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()

        def update(x, y, step):
            if x < 0 or x >= row or y < 0 or y >= col:
                return

            if step > grid[x][y]:
                return
            grid[x][y] = step
            q.append((x, y))
            

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))

        step = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                update(x+1, y, step+1)
                update(x-1, y, step+1)
                update(x, y-1, step+1)
                update(x, y+1, step+1)
            step += 1