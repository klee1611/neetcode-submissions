# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur, suf = None, slow.next, None
        slow.next = None
        while cur:
            suf = cur.next
            cur.next = prev
            prev = cur
            cur = suf

        l1, l2 = head, prev
        while l1 and l2:
            l1_s, l2_s = l1.next, l2.next
            l1.next = l2
            l2.next = l1_s
            l1, l2 = l1_s, l2_s
            