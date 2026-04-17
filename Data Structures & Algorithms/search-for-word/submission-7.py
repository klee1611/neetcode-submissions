class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row, col = len(board), len(board[0])
        
        visited = set()
        def dfs(x, y, idx):
            if idx == len(word):
                return True

            if not 0 <= x < row or not 0 <= y < col or \
                (x, y) in visited:
                return False

            if board[x][y] != word[idx]:
                return False

            visited.add((x, y))
            for dx, dy in directions:
                if dfs(x + dx, y + dy, idx + 1) == True:
                    return True
            visited.remove((x, y))

            return False

        for x in range(row):
            for y in range(col):
                if board[x][y] == word[0]:
                    if dfs(x, y, 0):
                        return True
                    visited = set()

        return False