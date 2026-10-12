class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in range(len(nums)):
            new_res = res[:]
            for sub in res:
                new_res.append(sub + [nums[i]])
            res = new_res

        return res