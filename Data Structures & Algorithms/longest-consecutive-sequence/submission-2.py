class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hash_set = set(nums)
        r = 0
        for n in nums:
            if n-1 not in hash_set:
                length = 1
                while n+length in hash_set:
                    length += 1
                print(n, length)
                r = max(r, length)
        return r