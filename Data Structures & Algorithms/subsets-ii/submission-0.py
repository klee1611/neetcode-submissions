class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []

        def backtrack(i, cur):
            nonlocal r
            if i >= len(nums):
                r.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtrack(i+1, cur)
            cur.pop()

            j = i
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            backtrack(j, cur)
            return

        backtrack(0, [])
        return r