class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        r = []
        def backtrack(i, cur):
            nonlocal r, nums
            if i == len(nums):
                r.append(cur.copy())
                return

            if i > len(nums):
                return

            for idx in range(i, len(nums)):
                cur[idx], cur[i] = cur[i], cur[idx]
                backtrack(i+1, cur)
                cur[i], cur[idx] = cur[idx], cur[i]

        backtrack(0, nums)
        return r