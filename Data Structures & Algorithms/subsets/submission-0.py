class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        for n in nums:
            if not r:
                r.append([n])
                continue
            
            for i in range(len(r)):
                l = r[i][:]
                l.append(n)
                r.append(l)
            r.append([n])
        r.append([])
        return r