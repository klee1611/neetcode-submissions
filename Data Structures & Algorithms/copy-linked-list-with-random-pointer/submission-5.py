"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}

        dummy = Node(0)
        old_n, new_n = head, dummy

        while old_n:
            if not nodes.get(old_n, None):
                nodes[old_n] = Node(old_n.val)
            if old_n.random and not nodes.get(old_n.random, None):
                nodes[old_n.random] = Node(old_n.random.val)
            if old_n.random:
                nodes[old_n].random = nodes[old_n.random]

            new_n.next = nodes[old_n]
            old_n, new_n = old_n.next, new_n.next

        return dummy.next