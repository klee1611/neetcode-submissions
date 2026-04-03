class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        climb = [ 0 for _ in range(n + 1) ]

        for i in range(2, n+1):
            climb[i] = min(cost[i-1] + climb[i-1], cost[i-2] + climb[i-2])
            print(climb)

        return climb[n]