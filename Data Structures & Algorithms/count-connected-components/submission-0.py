class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        visited = set()
        graph_count = 0

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        for i in range(n):
            if i not in visited:
                q = deque()
                q.append((-1, i))
                while q:
                    prev_node, node = q.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    for next_node in adj[node]:
                        q.append((node, next_node))
                graph_count += 1
        return graph_count