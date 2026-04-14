class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        row_zero, col_zero = False, False

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_zero = True
                    if j == 0:
                        col_zero = True
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, row):
            if matrix[i][0] == 0:
                for j in range(col):
                    matrix[i][j] = 0

        for i in range(1, col):
            if matrix[0][i] == 0:
                for j in range(row):
                    matrix[j][i] = 0

        if row_zero:
            for i in range(col):
                matrix[0][i] = 0

        if col_zero:
            for i in range(row):
                matrix[i][0] = 0
