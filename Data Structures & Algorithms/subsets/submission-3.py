class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            new_res = res[:]
            for r in res:
                l = r[:]
                l.append(n)
                new_res.append(l)
            res = new_res

        return res