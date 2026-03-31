# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r = ListNode()
        cur_1, cur_2, cur_r = l1, l2, r

        carry = 0
        while cur_1 and cur_2:
            cur_r.next = ListNode()
            cur_r = cur_r.next

            tmp = cur_1.val + cur_2.val + carry
            carry = 1 if tmp >= 10 else 0
            cur_r.val = tmp % 10
            cur_1, cur_2 = cur_1.next, cur_2.next

        cur = cur_1 if cur_1 else cur_2
        while cur:
            cur_r.next = ListNode()
            cur_r = cur_r.next

            tmp = cur.val + carry
            carry = 1 if tmp >= 10 else 0
            cur_r.val = tmp % 10
            cur = cur.next
        
        if carry:
            cur_r.next = ListNode()
            cur_r.next.val = 1

        return r.next
        
