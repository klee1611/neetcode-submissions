class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        max_len = 0
        seen = set()
        i, j = 0, 0

        while j < len(s):
            while s[j] in seen:
                if s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                seen.remove(s[i])
                i += 1

            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
            j += 1

        return max_len