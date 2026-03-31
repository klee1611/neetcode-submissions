class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []
        
        def dfs(i, cur, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                r.append(cur)
                return

            dfs(i+1, cur.copy(), total)
            cur.append(nums[i])
            dfs(i, cur.copy(), total+nums[i])

        dfs(0, [], 0)

        return r