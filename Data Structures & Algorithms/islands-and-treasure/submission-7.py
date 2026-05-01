class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        row, col = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    q.append((x, y, 0))
                    visited.add((x, y))

        while q:
            x, y, step = q.popleft()
            grid[x][y] = step
            for dx, dy in directs:
                x_1, y_1 = x + dx, y + dy
                if x_1 >= row or x_1 < 0 or y_1 >= col or y_1 < 0 or \
                    grid[x_1][y_1] == -1 or (x_1, y_1) in visited:
                    continue
                q.append((x_1, y_1, step + 1))
                visited.add((x_1, y_1))
            