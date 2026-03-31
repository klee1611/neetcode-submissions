class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if 1 == len(nums):
            return nums[0]
        if 2 == len(nums):
            return [nums[1], nums[0]]

        product = [ [1 for n in nums] for n in nums ]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    product[i][j] = nums[i]
                else:
                    product[i][j] = product[i][j-1] * nums[j]

        r = [product[1][len(nums)-1]]
        for i in range(1, len(nums)-1):
            r.append(product[0][i-1]*product[i+1][len(nums)-1])
        r.append(product[0][len(nums)-2])
        return r