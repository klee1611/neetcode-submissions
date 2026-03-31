# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1, l2 = [], []
        cur = head
        while cur:
            l1.append(cur)
            l2.append(cur)
            cur = cur.next
        l1.reverse()

        for i in range(len(l1)//2):
            l2[i].next = l1[i]
            if l2[i+1]:
                l1[i].next = l2[i+1]
        
        cur = l2[0]
        for i in range(len(l1)):
            cur = cur.next
        if cur and cur.next:
            cur.next.next = None

        return