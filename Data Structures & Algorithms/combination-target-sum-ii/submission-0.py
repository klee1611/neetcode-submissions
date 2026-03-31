class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        r = []

        def dfs(i, cur, total):
            if total == target:
                r.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            j = i+1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, cur, total)
            
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i])
            cur.pop()
            return

        dfs(0, [], 0)
        return r