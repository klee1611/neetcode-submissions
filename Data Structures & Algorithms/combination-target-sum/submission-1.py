class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []

        def backtrack(i, cur, total):
            nonlocal r
            if total == target:
                r.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            backtrack(i+1, cur, total)
            
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            cur.pop()
        backtrack(0, [], 0)

        return r