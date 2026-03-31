# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        r = 0
        def dfs(node):
            if not node:
                return 0
            
            nonlocal r
            lh, rh = dfs(node.left), dfs(node.right)
            r = max(r, lh+rh)
            return max(lh, rh) + 1
        dfs(root)
        return r