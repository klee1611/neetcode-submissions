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
            while map[node]:
                next_node = map[node].pop()
                if next_node == prev_node:
                    continue
                if not dfs(node, next_node):
                    return False
            return True
        dfs(None, 0)

        return len(visited) == n