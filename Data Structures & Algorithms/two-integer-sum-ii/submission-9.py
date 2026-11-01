class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        remain = {}
        for i, n in enumerate(numbers):
            if remain.get(n, None) is not None:
                return [remain[n]+1, i+1]
            remain[target-n] = i
        return []