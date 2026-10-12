class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if nums[0] > target:
            return []

        n = len(nums)
        res = []
        q = deque([(target, [], 0)])

        while q:
            cur_t, ans, idx = q.pop()
            if cur_t == 0:
                res.append(ans)
                continue

            for i in range(idx, n):
                if cur_t >= nums[i]:
                    new_ans = ans[:]
                    new_ans.append(nums[i])
                    q.append((cur_t - nums[i], new_ans, i))

        return res