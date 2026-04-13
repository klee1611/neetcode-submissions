class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        count = defaultdict(int)

        for n in nums:
            if count[n]:
                continue
            str_len = count[n-1] + count[n+1] + 1
            if count[n-1]:
                count[n - count[n-1]] = str_len
            if count[n+1]:
                count[n + count[n+1]] = str_len
            count[n] = str_len
            res = max(res, str_len)

        return res