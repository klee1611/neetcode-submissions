"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes_map = defaultdict(Node)

        visited = set()
        q = deque([node])

        while q:
            n = q.pop()
            if n in visited:
                continue
            visited.add(n)

            new_n = nodes_map[n]
            new_n.val = n.val
            for neighbor in n.neighbors:
                new_n.neighbors.append(nodes_map[neighbor])
                if not neighbor in visited:
                    q.append(neighbor)

        return nodes_map[node]