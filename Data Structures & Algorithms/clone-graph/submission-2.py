"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}

        def get_node(n):
            if not n:
                return

            if node_map.get(n.val, None):
                return node_map[n.val]

            new_n = Node(n.val)
            node_map[n.val] = new_n
            for neighbor in n.neighbors:
                new_neighbor = get_node(neighbor)
                new_n.neighbors.append(new_neighbor)

            return new_n

        return get_node(node)