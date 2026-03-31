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
    
        cur_1, cur_2 = head, prev
        while cur_2:
            cur_1_next = cur_1.next
            cur_2_next = cur_2.next 
            cur_1.next = cur_2
            cur_2.next = cur_1_next
            cur_1 = cur_1_next
            cur_2 = cur_2_next

