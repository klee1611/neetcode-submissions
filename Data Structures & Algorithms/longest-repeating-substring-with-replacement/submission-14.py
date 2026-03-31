class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l, r = 0, 0
        max_f = 0
        res = 0
        
        while r < len(s):
            count[ord(s[r]) - ord('A')] += 1
            max_f = max(max_f, count[ord(s[r]) - ord('A')])

            while r - l + 1 - max_f > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1

            if r - l + 1 - max_f <= k:
                res = max(res, r - l + 1) 

            r += 1

        return res