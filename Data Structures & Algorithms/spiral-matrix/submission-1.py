class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        res = []
        i, j, direct = 0, 0, 0
        for count in range(row * col):
            res.append(matrix[i][j])
            matrix[i][j] = 'x'
            dx, dy = directs[direct]
            if i + dx < 0 or i + dx >= row or j + dy < 0 or j + dy >= col or \
                matrix[i + dx][j + dy] == 'x':
                direct = (direct + 1) % 4
                dx, dy = directs[direct]
            i += dx
            j += dy

        return res