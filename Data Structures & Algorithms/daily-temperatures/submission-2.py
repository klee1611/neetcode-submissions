class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r = [0] * len(temperatures)

        for i in range(len(temperatures)-2, -1, -1):
            j = 1
            while i + j < len(temperatures):
                if temperatures[i + j] > temperatures[i]:
                    r[i] = j
                    break
                if r[i+j] == 0:
                    break
                if i + j == len(temperatures) - 1:
                    break
                j = r[i+j] + j
                print(r, i, j)
        return r