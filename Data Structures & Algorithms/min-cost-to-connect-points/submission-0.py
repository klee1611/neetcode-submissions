class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                adj[i][j] = adj[j][i] = max(x1, x2) - min(x1, x2) + max(y1, y2) - min(y1, y2)

        cost_heap = [(0, 0)]
        visited = set()
        total_cost = 0
        while len(visited) < n:
            cost, vertex = heapq.heappop(cost_heap)
            if vertex in visited:
                continue

            total_cost += cost
            visited.add(vertex)
            for i in range(n):
                if i == vertex:
                    continue
                heapq.heappush(cost_heap, (adj[vertex][i], i))

        return total_cost