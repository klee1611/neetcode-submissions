class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return 0

        adj = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi = points[i]
                xj, yj = points[j]
                adj[i][j] = adj[j][i] = abs(xi - xj) + abs(yi - yj)

        visited = set()
        r = 0
        heap = [(0, 0)]
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue

            r += dist
            visited.add(node)
            for i in range(n):
                if i in visited:
                    continue
                heapq.heappush(heap, (adj[node][i], i))

        return r