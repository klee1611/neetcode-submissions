class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        hash_table = defaultdict(int)
        start, max_len = 0, 0
        for i in range(len(s)):
            if s[i] not in hash_table:
                cur_len = i - start + 1
                max_len = max(cur_len, max_len)
            else:
                repeat_i = hash_table[s[i]]
                for j in range(start, repeat_i+1):
                    hash_table.pop(s[j])
                start = repeat_i + 1
            hash_table[s[i]] = i
        return max_len