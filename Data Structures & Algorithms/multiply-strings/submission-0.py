class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0] == "0" or num2[0] == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                r = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                res[i + j] += r
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        res.reverse()
        start = 0
        while res[start] == 0:
            start += 1
        
        return "".join([str(n) for n in res[start:]])        