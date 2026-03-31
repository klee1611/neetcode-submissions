class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        while i < j:
            cur_sum = numbers[i] + numbers[j]
            if cur_sum == target:
                return [i+1, j+1]
            if cur_sum < target:
                i += 1
            else:
                j -= 1