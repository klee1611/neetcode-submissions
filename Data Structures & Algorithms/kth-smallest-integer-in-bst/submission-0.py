# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        vals = []
        def dfs(node):
            nonlocal vals
            if not node:
                return

            if len(vals) > k:
                return
            if node.left:
                dfs(node.left)
            if len(vals) > k:
                return
            vals.append(node.val)
            if len(vals) > k:
                return
            if node.right:
                dfs(node.right)
            return
        dfs(root)

        return vals[k-1]