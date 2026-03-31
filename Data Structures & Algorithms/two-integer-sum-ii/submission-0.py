class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            t = target - numbers[i]
            for j in range(len(numbers)):
                if numbers[j] == t:
                    return [i+1, j+1]