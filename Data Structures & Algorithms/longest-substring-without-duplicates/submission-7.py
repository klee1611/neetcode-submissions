class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        counts = defaultdict(int)
        l, r = 0, 1
        counts[s[0]] = 1
        res = 0
        while r < n:
            while counts[s[r]]:
                counts[s[l]] -= 1
                l += 1
            counts[s[r]] += 1
            res = max(res, r - l + 1)
            r += 1
        return res