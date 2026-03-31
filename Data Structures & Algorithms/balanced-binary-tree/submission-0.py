# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = True
        def treeH(node):
            if not node:
                return 0

            nonlocal balanced
            l_h, r_h = treeH(node.left), treeH(node.right)
            balanced = False if abs(l_h - r_h) > 1 else balanced
            return 1 + max(l_h, r_h)
        treeH(root)

        return balanced