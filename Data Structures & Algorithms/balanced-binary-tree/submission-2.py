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

        res = True

        def height(node):
            if not node:
                return 0

            hl, hr = height(node.left), height(node.right)
            nonlocal res
            if abs(hl - hr) > 1:
                res = False

            return 1 + max(hl, hr)

        height(root)
        return res