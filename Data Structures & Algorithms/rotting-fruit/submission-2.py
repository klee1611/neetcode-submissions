class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        q = deque()

        row, col = len(grid), len(grid[0])

        max_t = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            x, y, t = q.popleft()
            for dx, dy in directs:
                n_x, n_y = x + dx, y + dy
                if 0 <= n_x < row and 0 <= n_y < col and grid[n_x][n_y] == 1:
                    grid[n_x][n_y] = 2
                    max_t = max(max_t, t + 1)
                    q.append((n_x, n_y, t + 1))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return max_t
            