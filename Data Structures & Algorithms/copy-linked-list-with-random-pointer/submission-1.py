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
        if not head:
            return None
            
        table = defaultdict(Node)
        cur = head
        while cur:
            table[cur] = Node(cur.val)
            cur = cur.next

        for origin, copy in table.items():
            if origin.next:
                copy.next = table[origin.next]
            if origin.random:
                copy.random = table[origin.random]

        return table[head]