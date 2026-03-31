class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        from_matrix = lambda x, y: x * n + y
        to_matrix = lambda index: (index // n, index % n)

        i, j = 0, m * n
        while i < j:
            mid = (i+j) // 2
            mat_i, mat_j = to_matrix(mid)
            if matrix[mat_i][mat_j] == target:
                return True
            elif matrix[mat_i][mat_j] < target:
                i = mid + 1
            else:
                j = mid
        return False