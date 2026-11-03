class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []

        def tracking(idx, cur, remain):
            if remain == 0:
                res.append(cur[:])
                return

            if idx == n or remain < 0:
                return

            cur.append(nums[idx])
            tracking(idx, cur, remain - nums[idx])
            cur.pop()
            tracking(idx+1, cur, remain)

        tracking(0, [], target)
        return res