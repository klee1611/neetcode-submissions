class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hash_map = defaultdict(int)
        for n in nums:
            if not hash_map[n]:
                length = hash_map[n-1] + hash_map[n+1] + 1
                hash_map[n] = length
                hash_map[n - hash_map[n-1]] = length
                hash_map[n + hash_map[n+1]] = length
                print(hash_map)

        return max([v for v in hash_map.values()])