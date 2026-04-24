class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = len(temperatures)
        res = [0] * days

        for i in range(days-2, -1, -1):
            j = i + 1
            while j < days:
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                if not res[j]:
                    break
                j += res[j]

        return res