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
        while cur_1 or cur_2 or carry:
            cur_r.next = ListNode()
            cur_r = cur_r.next

            v1 = cur_1.val if cur_1 else 0
            v2 = cur_2.val if cur_2 else 0
            tmp = v1 + v2 + carry
            carry = 1 if tmp >= 10 else 0
            cur_r.val = tmp % 10

            cur_1 = cur_1.next if cur_1 else None
            cur_2 = cur_2.next if cur_2 else None

        return r.next
        
