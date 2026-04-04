class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1

        n = len(gas)
        remain = [0] * n
        for i in range(n):
            remain[i] = gas[i] - cost[i]

        total = 0
        start = 0
        for i in range(n):
            total += remain[i]
            if total < 0:
                start = i+1
                total = 0

        return start