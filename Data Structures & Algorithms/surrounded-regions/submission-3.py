class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row, col = len(board), len(board[0])

        def dfs(x, y, nodes):
            if not 0 <= x < row or not 0 <= y < col or \
                (x, y) in nodes or board[x][y] != "O":
                return True

            flip = True
            if 0 == x or 0 == y or x == row - 1 or y == col - 1:
                flip = False

            nodes.add((x, y))
            board[x][y] = "A"
            for dx, dy in directs:
                if not dfs(x + dx, y + dy, nodes):
                    flip = False
            
            return flip

        for x in range(row):
            for y in range(col):
                nodes = set()
                if board[x][y] == "O":
                    flip = dfs(x, y, nodes)
                    if flip:
                        for x1, y1 in nodes:
                            board[x1][y1] = "X"

        for x in range(row):
            for y in range(col):
                if board[x][y] == "A":
                    board[x][y] = "O"