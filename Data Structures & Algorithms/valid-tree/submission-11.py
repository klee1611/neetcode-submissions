class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list[v2].append(v1)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for v in adj_list[node]:
                if v == prev:
                    continue
                if not dfs(v, node):
                    return False

            return True
        
        if not dfs(0, None):
            return False

        return len(visited) == n