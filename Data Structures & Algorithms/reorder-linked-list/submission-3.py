# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next

        i, j = 0, len(l)-1
        while i < j:
            l[i].next = l[j]
            
            i += 1
            if i >= j:
                break
            l[j].next = l[i]
            j -= 1
        
        l[i].next = None