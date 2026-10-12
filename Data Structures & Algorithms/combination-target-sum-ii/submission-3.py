class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        q = deque([(target, [], 0)])
        while q:
            cur_t, ans, idx = q.pop()
            if cur_t == 0:
                res.append(ans[:])
                continue
            if cur_t < 0 or idx >= n:
                continue

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] <= cur_t:
                    next_ans = ans[:]
                    next_ans.append(candidates[i])
                    q.append((cur_t - candidates[i], next_ans, i+1))
       
        return res