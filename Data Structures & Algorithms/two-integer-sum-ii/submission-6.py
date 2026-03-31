class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            r = numbers[i] + numbers[j]
            if r == target:
                return [i+1, j+1]
            if r < target:
                i += 1
            if r > target:
                j -= 1
        return None