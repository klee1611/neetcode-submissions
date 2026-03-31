class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [ set() for i in range(9) ]
        col = [ set() for i in range(9) ]
        grid = [ set() for i in range(9) ]

        def which_grid(i, j):
            return i // 3 * 3 + j // 3

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in row[i] or board[i][j] in col[j] or
                 board[i][j] in grid[which_grid(i, j)]):
                    print(i, j)
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                grid[which_grid(i, j)].add(board[i][j])

        return True