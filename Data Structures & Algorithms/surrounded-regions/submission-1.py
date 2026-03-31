class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(x, y):
            if min(x, y) < 0 or x >= row or y >= col or \
                board[x][y] != 'O':
                return

            board[x][y] = 'S'
            for dx, dy in directs:
                dfs(dx+x, dy+y)


        for x in range(row):
            dfs(x, 0)
            dfs(x, col-1)

        for y in range(col):
            dfs(0, y)
            dfs(row-1, y)

        for x in range(row):
            for y in range(col):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'S':
                    board[x][y] = 'O'
            