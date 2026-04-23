# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            res = l1.val + l2.val + carry
            cur.next = ListNode(res % 10)
            carry = res // 10
            l1, l2, cur = l1.next, l2.next, cur.next

        l = l1 or l2
        while l:
            res = l.val + carry
            cur.next = ListNode(res % 10)
            carry = res // 10
            l, cur = l.next, cur.next

        if carry:
            cur.next = ListNode(1)

        return dummy.next