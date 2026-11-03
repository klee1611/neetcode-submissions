class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def tracking(idx, cur, remain):
            if remain == 0:
                res.append(cur[:])
                return

            if idx >= n or remain < 0:
                return

            cur.append(candidates[idx])
            tracking(idx + 1, cur, remain - candidates[idx])
            cur.pop()
            while idx < n - 1 and candidates[idx+1] == candidates[idx]:
                idx += 1
            tracking(idx + 1, cur, remain)

        tracking(0, [], target)
        return res