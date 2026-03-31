# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode()
        cur1, cur2, cur = l1, l2, dummy
        carry = 0
        while cur1 or cur2:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0
            val = v1 + v2 + carry
            node = ListNode(val % 10)
            carry = 1 if val >= 10 else 0
            cur.next = node
            cur = node
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None

        if carry:
            cur.next = ListNode(1)
        return dummy.next