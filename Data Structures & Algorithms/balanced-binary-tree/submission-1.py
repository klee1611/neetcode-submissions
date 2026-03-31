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
        def dfs(node):
            if not node:
                return 0

            nonlocal res
            l, r = dfs(node.left), dfs(node.right)
            if abs(l - r) > 1:
                res = False
            return max(dfs(node.left), dfs(node.right)) + 1
        dfs(root)
        return res