class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)

        i, j, res = 0, 0, 0
        max_f, count = 0, defaultdict(int)
        count[s[j]] += 1
        while j < len(s):
            cur_len = j - i + 1
            tmp = max(count, key = lambda x: count[x])
            max_f = count[tmp]
            if cur_len - max_f <= k:
                res = max(res, cur_len)
                j += 1
                if j < len(s):
                    count[s[j]] += 1
            else:
                count[s[i]] -= 1
                i += 1
        
        return res