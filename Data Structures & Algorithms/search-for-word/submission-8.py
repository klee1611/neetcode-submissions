class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        row, col = len(board), len(board[0])
        n = len(word)

        def track(x, y, idx):
            if idx >= n:
                return True

            if x < 0 or x >= row or y < 0 or y >= col \
                or board[x][y] != word[idx]:
                return False

            board[x][y] = "?"
            for dx, dy in dirs:
                new_x, new_y = x + dx, y + dy
                if track(new_x, new_y, idx+1):
                    return True

            board[x][y] = word[idx]
            return False
        
        for x in range(row):
            for y in range(col):
                if board[x][y] == word[0]:
                    if track(x, y, 0):
                        return True
        return False