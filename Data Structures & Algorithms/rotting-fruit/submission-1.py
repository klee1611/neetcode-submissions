class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count, turns = 0, 0
        directs = [(0, -1), (0,  1), (-1, 0), (1, 0)]
        row, col = len(grid), len(grid[0])
        q = deque()

        def rotting(x, y):
            if min(x, y) < 0 or x >= row or y >= col or grid[x][y] != 1:
                return
            nonlocal fresh_count, q
            fresh_count -= 1
            grid[x][y] = 2
            q.append((x, y))
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh_count += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        if len(q) == 0:
            return -1 if fresh_count > 0 else 0

        while q:
            for r in range(len(q)):
                i, j = q.popleft()
                for ni, nj in directs:
                    rotting(i + ni, j + nj)
            turns += 1

        return -1 if fresh_count > 0 else turns-1