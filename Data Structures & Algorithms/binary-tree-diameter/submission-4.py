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
            
        max_dia = 0
        def hight(node):
            if not node:
                return 0

            h_l = 1 + hight(node.left) if node.left else 0
            h_r = 1 + hight(node.right) if node.right else 0
            nonlocal max_dia
            max_dia = max(max_dia, h_l + h_r)
            
            return max(h_l, h_r)
        hight(root)

        return max_dia