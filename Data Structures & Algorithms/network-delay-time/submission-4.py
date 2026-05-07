class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for v1, v2, t in times:
            adj[v1].append((v2, t))

        reach_t = [(0, k)]
        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        visited = set()
        while reach_t:
            t, node = heapq.heappop(reach_t)
            if node in visited:
                continue
            visited.add(node)

            for next_node, time in adj[node]:
                if next_node in visited:
                    continue
                dist[next_node] = min(dist[next_node], t + time)
                heapq.heappush(reach_t, (dist[next_node], next_node))

        res = max(dist[1:])
        return res if res < float("inf") else -1