class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for next_node in adj[node]:
                dfs(next_node)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count