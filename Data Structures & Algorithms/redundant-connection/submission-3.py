class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = defaultdict(list)
        indegrees = [0] * (n + 1)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
            indegrees[v1] += 1
            indegrees[v2] += 1

        q = deque()
        for i in range(n+1):
            if indegrees[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            indegrees[node] -= 1
            for next_node in adj[node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 1:
                    q.append(next_node)

        edges.reverse()
        for v1, v2 in edges:
            if indegrees[v1] == 2 and indegrees[v2] == 2:
                return [v1, v2]