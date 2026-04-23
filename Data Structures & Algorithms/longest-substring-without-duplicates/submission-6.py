class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        l, r = 0, 0
        max_len = 0
        exist = set()

        while r < len(s):
            if s[r] not in exist:
                max_len = max(max_len, r - l + 1)
                exist.add(s[r])
                r += 1
                continue

            while s[r] in exist:
                exist.remove(s[l])
                l += 1
            exist.add(s[r])
            r += 1

        return max_len