class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        def backtrack(idx, cur):
            if idx > n:
                return
            if idx == n:
                res.append(cur[:])
                return

            i = idx + 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
            backtrack(i, cur)

            cur.append(nums[idx])
            backtrack(idx+1, cur)
            cur.pop()
        backtrack(0, [])
                
        return res