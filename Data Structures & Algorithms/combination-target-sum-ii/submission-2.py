class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(cur_t, ans, idx):
            if cur_t == 0:
                res.append(ans[:])
                return
            if cur_t < 0 or idx >= n:
                return 

            ans.append(candidates[idx])
            backtrack(cur_t - candidates[idx], ans, idx + 1)
            ans.pop()

            while idx + 1 < n and candidates[idx] == candidates[idx+1]:
                idx += 1
            backtrack(cur_t, ans, idx+1)
        backtrack(target, [], 0)
       
        return res