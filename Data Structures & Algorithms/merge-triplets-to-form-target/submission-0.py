class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        len_t = len(triplets)
        if len_t < 2:
            return triplets[0] == target

        r = [False] * 3
        for t1, t2, t3 in triplets:
            if t1 > target[0] or t2 > target[1] or t3 > target[2]:
                continue
            if t1 == target[0]:
                r[0] = True
            if t2 == target[1]:
                r[1] = True
            if t3 == target[2]:
                r[2] = True

        return r[0] == r[1] == r[2] == True        