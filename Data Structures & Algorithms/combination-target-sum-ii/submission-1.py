class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(idx, remain, nums):
            if remain == 0:
                res.append(nums[:])
                return

            if idx == n or candidates[idx] > remain:
                return

            nums.append(candidates[idx])
            backtrack(idx + 1, remain - candidates[idx], nums)
            nums.pop()
            
            while idx < n - 1 and candidates[idx+1] == candidates[idx]:
                idx += 1
            backtrack(idx + 1, remain, nums)

        backtrack(0, target, [])
        return res