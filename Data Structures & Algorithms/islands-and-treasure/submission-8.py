class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x in range(row):
            for y in range(col):
                if grid[x][y] == 0:
                    q.append((x, y))

        step = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                if (x, y) in visited:
                    continue

                visited.add((x, y))
                grid[x][y] = step
                for dx, dy in directs:
                    p = (x + dx, y + dy)
                    if p[0] < 0 or p[1] < 0 or p[0] >= row or p[1] >= col:
                        continue
                    if p in visited or grid[p[0]][p[1]] == -1:
                        continue

                    q.append(p)
            step += 1