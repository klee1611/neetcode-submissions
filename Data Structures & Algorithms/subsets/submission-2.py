class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = [[]]
        for n in nums:
            for i in range(len(r)):
                r.append(r[i].copy() + [n])
        return r