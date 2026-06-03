class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        r = 0
        heap = [(0, k)]
        while heap:
            t_n, node = heapq.heappop(heap)
            if node in visited:
                continue

            visited.add(node)
            r = max(t_n, r)
            for v, t_v in adj[node]:
                if v in visited:
                    continue

                heapq.heappush(heap, (t_v + t_n, v))

        return -1 if len(visited) != n else r