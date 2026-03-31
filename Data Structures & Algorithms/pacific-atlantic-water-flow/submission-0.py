class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dir_pac = {(-1, 0), (0, -1)}
        dir_atl = {(1, 0), (0, 1)}
        row, col = len(heights), len(heights[0])
        set_pac, set_atl = set(), set()
        
        def dfs(x, y, ocean_set, prev_height):
            if min(x, y) < 0 or (x, y) in ocean_set or x >= row \
                or y >= col or prev_height > heights[x][y]:
                return
            
            ocean_set.add((x, y))
            dfs(x-1, y, ocean_set, heights[x][y])
            dfs(x+1, y, ocean_set, heights[x][y])
            dfs(x, y-1, ocean_set, heights[x][y])
            dfs(x, y+1, ocean_set, heights[x][y])

        for x in range(row):
            dfs(x, 0, set_pac, heights[x][0])
            dfs(x, col-1, set_atl, heights[x][col-1])

        for y in range(col):
            dfs(0, y, set_pac, heights[0][y])
            dfs(row-1, y, set_atl, heights[row-1][y])

        r = []
        for x in range(row):
            for y in range(col):
                if (x, y) in set_pac and (x, y) in set_atl:
                    r.append([x, y])

        return r