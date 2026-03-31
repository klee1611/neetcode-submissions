# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, cur, suf = None, head, head.next
        while suf:
            cur.next = prev
            prev = cur
            cur = suf
            suf = suf.next
        cur.next = prev

        return cur