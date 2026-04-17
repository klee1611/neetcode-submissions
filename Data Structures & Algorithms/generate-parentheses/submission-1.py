class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(start, close, current):
            if not start and not close:
                return [current]

            r = []
            if start:
                r += dfs(start-1, close+1, current+"(")

            if close:
                r += dfs(start, close-1, current+")")

            return r               

        return dfs(n, 0, "")