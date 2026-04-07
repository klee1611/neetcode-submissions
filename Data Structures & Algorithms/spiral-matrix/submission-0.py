class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 1:
            return matrix[0]
        m = len(matrix[0])

        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = []
        x, y, count, d_idx = 0, 0, 0, 0
        while count < n * m:
            res.append(matrix[x][y])
            count += 1
            matrix[x][y] = -101
            dx, dy = directs[d_idx]
            if 0 > min(x + dx, y + dy) or n <= x + dx or m <= y + dy or \
                matrix[x+dx][y+dy] == -101:
                d_idx = (d_idx + 1) % 4
                dx, dy = directs[d_idx]
            x += dx
            y += dy

        return res