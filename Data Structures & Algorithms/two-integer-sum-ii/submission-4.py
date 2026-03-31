class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            t = target - numbers[i]
            j, k = i, len(numbers)
            while j < k:
                mid = (j + k) // 2
                print(f"t={t}, i={i}, j={j}, k={k}, mid={mid}, numbers[i]={numbers[i]}, numbers[mid]={numbers[mid]}")
                if numbers[mid] == t:
                    return [i+1, mid+1]
                if numbers[mid] < t:
                    j = mid+1
                else:
                    k = mid