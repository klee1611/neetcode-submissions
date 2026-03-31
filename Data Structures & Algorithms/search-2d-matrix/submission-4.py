class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        to_one_dim = lambda x, y: x * m + y
        from_one_dim = lambda x: (x // m, x % m)

        l, r = 0, n * m
        while l < r:
            mid = (l + r) // 2
            x, y = from_one_dim(mid)
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid
        return False