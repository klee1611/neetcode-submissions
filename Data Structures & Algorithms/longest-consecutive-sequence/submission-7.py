class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_len = 0
        boundary_len = defaultdict(int)
        for n in nums_set:
            if boundary_len[n]:
                continue
            boundary_len[n] = boundary_len[n-1] + boundary_len[n+1] + 1
            boundary_len[n - boundary_len[n-1]] = boundary_len[n]
            boundary_len[n + boundary_len[n+1]] = boundary_len[n]
            max_len = max(max_len, boundary_len[n])
        
        return max_len