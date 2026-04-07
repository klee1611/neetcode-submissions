class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        x_zero, y_zero = False, False
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == 0:
                    if x == 0:
                        x_zero = True
                    if y == 0:
                        y_zero = True
                    matrix[0][y] = 0
                    matrix[x][0] = 0

        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][0] == 0 or matrix[0][y] == 0:
                    matrix[x][y] = 0

        if x_zero:
            for y in range(n):
                matrix[0][y] = 0
        if y_zero:
            for x in range(m):
                matrix[x][0] = 0