class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        count = defaultdict(int)

        max_f = 1
        max_len = 1
        i, j = 0, 0
        count[s[0]] = 1
        while j < len(s):
            while j - i + 1 - max_f > k:
                count[s[i]] -= 1
                i += 1
            j += 1
            if j < len(s):
                count[s[j]] += 1
                max_f = max(max_f, count[s[j]])
                if j - i + 1 - max_f <= k:
                    max_len = max(max_len, j - i + 1)

        return max_len
            