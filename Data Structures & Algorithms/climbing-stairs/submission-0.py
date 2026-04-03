class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        climb = [ float('inf') for _ in range(n+1) ]
        climb[0], climb[1], climb[2] = 0, 1, 2

        for i in range(3, n+1):
            climb[i] = climb[i-1] + climb[i-2]

        return climb[n]