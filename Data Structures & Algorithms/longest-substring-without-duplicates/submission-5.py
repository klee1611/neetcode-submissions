class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        res = 0
        l, r = 0, 0
        chs = set()
        while r < len(s):
            while s[r] in chs:
                chs.remove(s[l])
                l += 1
            chs.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res