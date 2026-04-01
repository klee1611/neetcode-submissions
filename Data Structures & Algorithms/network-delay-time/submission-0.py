class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        delay = [float('inf') for i in range(n+1)]
        delay[k] = 0

        for i in range(n):
            for source_v, dist_v, time in times:
                delay[dist_v] = min(delay[dist_v], delay[source_v] + time)

        max_delay = max(delay[1:])
        return max_delay if max_delay < float('inf') else -1