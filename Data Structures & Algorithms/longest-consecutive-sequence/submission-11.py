class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        res = 0
        bound_len = defaultdict(int)
        for n in nums:
            if bound_len[n]:
                continue
            bound_len[n] = bound_len[n-1] + bound_len[n+1] + 1
            bound_len[n - bound_len[n-1]] = bound_len[n]
            bound_len[n + bound_len[n+1]] = bound_len[n]
            res = max(res, bound_len[n])

        return res