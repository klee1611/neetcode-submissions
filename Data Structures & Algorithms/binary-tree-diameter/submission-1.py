# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_len = 0
        def treeH(node):
            if not node:
                return 0

            nonlocal max_len

            l_h, r_h = treeH(node.left), treeH(node.right)
            max_len = max(max_len, l_h + r_h)
            return 1 + max(l_h, r_h)
        treeH(root)

        return max_len