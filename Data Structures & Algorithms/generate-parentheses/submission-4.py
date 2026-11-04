class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(openC, closeC, cur):
            if openC > closeC:
                return

            if not openC and not closeC:
                res.append("".join(cur))
                return
            
            if openC:
                cur.append("(")
                helper(openC-1, closeC, cur)
                cur.pop()

            if closeC:
                cur.append(")")
                helper(openC, closeC-1, cur)
                cur.pop()

        helper(n, n, [])
        return res