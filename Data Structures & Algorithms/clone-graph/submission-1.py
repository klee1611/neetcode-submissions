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

        exist = {}
        def dfs(n):
            if n.val in exist:
                return exist[n.val]

            new_n = Node(n.val)
            exist[n.val] = new_n
            if not n.neighbors:
                return new_n

            for next_n in n.neighbors:
                if next_n.val in exist:
                    new_n.neighbors.append(exist[next_n.val])
                    continue
                
                new_n.neighbors.append(dfs(next_n))
            return new_n

        return dfs(node)