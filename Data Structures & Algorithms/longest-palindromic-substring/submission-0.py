class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        s_len = len(s)
        res, max_len = "", 0
        def check(l, r):
            nonlocal res, max_len
            while l >= 0 and r < s_len and s[l] == s[r]:
                str_len = r - l + 1
                if str_len > max_len:
                    res = s[l:r+1]
                    max_len = str_len
                l -= 1
                r += 1

        for i in range(s_len):
            l, r = i, i
            check(l, r)

            l, r = i, i+1
            check(l, r)

        return res