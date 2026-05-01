# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val or root.val == q.val:
            return root

        low, high = min(p.val, q.val), max(p.val, q.val)
        if low < root.val < high:
            return root

        if root.val > high:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return self.lowestCommonAncestor(root.right, p, q)