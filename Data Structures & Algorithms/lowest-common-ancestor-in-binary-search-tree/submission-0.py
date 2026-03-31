# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        m, n = max(p.val, q.val), min(p.val, q.val)
        if root.val > m:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < n:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
