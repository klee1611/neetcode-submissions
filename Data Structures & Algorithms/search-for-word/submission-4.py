class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        X, Y = len(board), len(board[0])
        path = set()

        def backtrack(i, x, y):
            if i == len(word):
                return True

            if x < 0 or y < 0 or x >= X or y >= Y or \
                board[x][y] != word[i] or (x, y) in path:
                return False

            path.add((x, y))
            r = backtrack(i+1, x+1, y) or \
                backtrack(i+1, x-1, y) or \
                backtrack(i+1, x, y+1) or \
                backtrack(i+1, x, y-1)
            path.remove((x, y))
            return r
        
        for i in range(X):
            for j in range(Y):
                if backtrack(0, i, j):
                    return True

        return False