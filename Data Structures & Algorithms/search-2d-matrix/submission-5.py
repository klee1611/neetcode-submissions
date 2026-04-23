class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        l_row, r_row, l_col, r_col = 0, row, 0, col
        res_row, res_col = -1, -1
        while l_row < r_row:
            mid = (l_row + r_row) // 2
            if matrix[mid][-1] < target:
                l_row = mid + 1
            else:
                res_row = mid
                r_row = mid

        while l_col < r_col:
            mid = (l_col + r_col) // 2
            if matrix[res_row][mid] == target:
                return True
            if matrix[res_row][mid] < target:
                l_col = mid + 1
            else:
                r_col = mid

        return False