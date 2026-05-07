class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i][j] = dist
                adj[j][i] = dist

        min_heap = [(0, 0)]
        visited = set()
        res = 0
        while len(visited) < n:
            dist, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            res += dist
            visited.add(node)
            for next_node in range(n):
                cost = adj[node][next_node]
                if next_node in visited:
                    continue
                heapq.heappush(min_heap, (cost, next_node))
        return res