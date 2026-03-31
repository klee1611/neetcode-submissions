class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res, max_f = 0, 0
        count = [0] * 26
        while r < len(s):
            index = ord(s[r]) - ord('A')
            count[index] += 1
            max_f = max(max_f, count[index])
            
            while r - l + 1 - max_f > k:
                index2 = ord(s[l]) - ord('A')
                count[index2] -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res