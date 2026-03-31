class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return

            for j in range(i, len(s)):
                l, r, is_p = i, j, True
                while r >= l:
                    if s[l] != s[r]:
                        is_p = False
                        break
                    r -= 1
                    l += 1
                if is_p:
                    cur.append(s[i:j+1])
                    backtrack(j+1, cur)
                    cur.pop()
        backtrack(0, [])
        return res            