class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [ set() for i in range(9) ]
        col = [ set() for i in range(9) ]
        grid = [ set() for i in range(9) ]

        def grid_num(i, j):
            return i // 3 * 3 + j // 3

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if '.' == n:
                    continue
                if n in row[i]:
                    return False
                if n in col[j]:
                    return False
                if n in grid[grid_num(i, j)]:
                    return False
                row[i].add(n)
                col[j].add(n)
                grid[grid_num(i,j)].add(n)

        return True






