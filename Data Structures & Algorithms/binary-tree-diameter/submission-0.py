# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeH(self, root: Optional[TreeNode], max_len: int):
        if not root:
            return (max_len, 0)

        l_max_len, l_h = self.treeH(root.left, max_len)
        r_max_len, r_h = self.treeH(root.right, max_len)
        max_len = max(max_len, l_h + r_h, l_max_len, r_max_len)
        return (max_len, 1 + max(l_h, r_h))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.treeH(root, 0)[0]