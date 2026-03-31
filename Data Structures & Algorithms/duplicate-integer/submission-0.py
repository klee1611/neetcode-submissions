class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for n in nums:
            if hash.get(n) is None:
                hash[n] = True
            else:
                return True
        return False