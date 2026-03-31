# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        m, n = max(p.val, q.val), min(p.val, q.val)
        cur = root
        while cur:
            if cur.val > m:
                cur = cur.left
                continue
            if cur.val < n:
                cur = cur.right
                continue
            return cur
        return None
