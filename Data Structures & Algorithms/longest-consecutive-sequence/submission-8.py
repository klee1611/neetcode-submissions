class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_len = 0
        for n in nums:
            if n-1 in nums_set:
                continue
            length = 0
            while n+length in nums_set:
                length += 1
            max_len = max(max_len, length)
        return max_len