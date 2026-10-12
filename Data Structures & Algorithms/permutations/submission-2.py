class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return [nums]

        res = []
        def permute(idx, ans):
            if idx == n:
                res.append(ans[:])

            for i in range(idx, n):
                ans[idx], ans[i] = ans[i], ans[idx]
                permute(idx+1, ans)
                ans[idx], ans[i] = ans[i], ans[idx]

        permute(0, nums)
        return res