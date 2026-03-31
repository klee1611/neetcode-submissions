class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            j = i+1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    r[i] = j - i
                    break
                if r[j] == 0:
                    break
                j += r[j]
            
        return r