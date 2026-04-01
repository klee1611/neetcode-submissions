class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        cycle_nodes = set()
        visited = set()
        map = defaultdict(list)

        for e in edges:
            map[e[0]].append(e[1])
            map[e[1]].append(e[0])

        def dfs_find_cycle_start(prev_node, node):
            if node in visited:
                return node

            visited.add(node)
            for n in map[node]:
                if n == prev_node:
                    continue

                start_node = dfs_find_cycle_start(node, n)
                if start_node != -1:
                    cycle_nodes.add(node)
                    return -1 if start_node == node else start_node
            return -1

        dfs_find_cycle_start(0, 1)
        for e in reversed(edges):
            if e[0] in cycle_nodes and e[1] in cycle_nodes:
                return e
        
        return []