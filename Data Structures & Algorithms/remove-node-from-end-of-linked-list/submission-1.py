# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        if length == n:
            return head.next

        length -= n
        cur = head
        for i in range(length):
            if i == length-1:
                tmp = cur.next.next
                cur.next = tmp
            cur = cur.next
        return head