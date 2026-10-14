class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        res = []
        def backtrack(start, end, ans):
            if start == 0 and end == 0:
                res.append(ans[:])
                return
            if end == 0:
                return
            if start > end:
                return

            if start > 0:
                ans.append("(")
                backtrack(start-1, end, ans)
                ans.pop()
            if end > 0:
                ans.append(")")
                backtrack(start, end-1, ans)
                ans.pop()

        backtrack(n-1, n, ["("])
        return [ "".join(p) for p in res ]