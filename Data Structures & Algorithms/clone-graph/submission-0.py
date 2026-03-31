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

        new_nodes = {}

        def create(new_node, old_node):
            new_node.val = old_node.val
            new_nodes[old_node.val] = new_node
            if not old_node.neighbors:
                return
            for n in old_node.neighbors:
                new_n = new_nodes.get(n.val, None)
                if not new_n:
                    new_n = Node()
                    create(new_n, n)
                new_node.neighbors.append(new_n)

        head = Node()
        create(head, node)
        return head