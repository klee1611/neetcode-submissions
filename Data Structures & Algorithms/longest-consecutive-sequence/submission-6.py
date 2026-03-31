class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        r = 0
        length = defaultdict(int)
        for n in nums:
            if not length[n]:
                length[n] = length[n-1] + length[n+1] + 1
                length[n - length[n-1]] = length[n]
                length[n + length[n+1]] = length[n]
                print(n, length[n])

            if length[n] > r:
                r = length[n]

        return r