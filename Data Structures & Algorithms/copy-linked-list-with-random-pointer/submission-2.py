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

        table = defaultdict(lambda: Node(0))
        cur = head
        while cur:
            table[cur].val = cur.val
            if cur.next:
                table[cur].next = table[cur.next]
            if cur.random:
                table[cur].random = table[cur.random]
            cur = cur.next

        return table[head]