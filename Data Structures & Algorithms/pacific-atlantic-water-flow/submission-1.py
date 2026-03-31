class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        set_pac, set_atl = set(), set()
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(init_data, ocean_set):
            q = deque(init_data)

            while q:
                x, y = q.popleft()
                ocean_set.add((x, y))
                for dx, dy in directs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and \
                        (nx, ny) not in ocean_set and \
                        heights[x][y] <= heights[nx][ny]:
                        q.append((nx, ny))

        init_pac, init_atl = [], []
        for x in range(row):
            init_pac.append((x, 0))
            init_atl.append((x, col-1))

        for y in range(col):
            init_pac.append((0, y))
            init_atl.append((row-1, y))

        bfs(init_pac, set_pac)
        bfs(init_atl, set_atl)

        r = []
        for x in range(row):
            for y in range(col):
                if (x, y) in set_pac and (x, y) in set_atl:
                    r.append([x, y])

        return r