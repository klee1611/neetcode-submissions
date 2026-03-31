class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False

        map = defaultdict(list)
        for e in edges:
            map[e[0]].append(e[1])
            map[e[1]].append(e[0])

        visited = set()
        def dfs(prev_node, node):
            nonlocal visited
            if node in visited:
                return False
            visited.add(node)
            if prev_node is not None:
                i = map[node].index(prev_node)
                del map[node][i]
            while map[node]:
                if not dfs(node, map[node].pop()):
                    return False
            return True
        dfs(None, 0)

        return len(visited) == n