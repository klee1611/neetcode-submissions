class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for v1, v2, t in times:
            adj[v1].append((v2, t))

        delays = [float('inf') for i in range(n+1)]
        delays[k] = 0

        edges_heap = [(0, k)]
        heapq.heapify(edges_heap)
        visited = set()

        while edges_heap:
            time, vertice = heapq.heappop(edges_heap)
            if vertice in visited:
                continue

            delays[vertice] = min(delays[vertice], time)
            visited.add(vertice)

            for node, t in adj[vertice]:
                if node in visited:
                    continue
                heapq.heappush(edges_heap, (t + time, node))

        return -1 if len(visited) != n else max(delays[1:])