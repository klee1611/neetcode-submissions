class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = [[]]
        for n in nums:
            for i in range(len(r)):
                l = r[i][:]
                l.append(n)
                r.append(l)
        return r