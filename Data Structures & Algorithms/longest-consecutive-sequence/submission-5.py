class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hash_set = set(nums)
        all_l = []
        for n in nums:
            if n-1 in hash_set:
                continue
            l = 1
            while n+1 in hash_set:
                l += 1
                n += 1
            all_l.append(l)
        
        return max(all_l)