class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        res = 0
        for i in range(len(s)):
            max_f, count = 0, defaultdict(int)
            for j in range(i, len(s)):
                count[s[j]] += 1
                max_f = max(max_f, count[s[j]])
                cur_len = j - i + 1
                if cur_len - max_f <= k:
                    res = max(res, cur_len)

        return res