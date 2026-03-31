class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        i, j = 0, 0
        res = 0
        max_f = 0
        count = defaultdict(int)
        while j < len(s):
            count[s[j]] += 1
            max_f = max(max_f, count[s[j]])
            while j - i + 1 - max_f > k:
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res
