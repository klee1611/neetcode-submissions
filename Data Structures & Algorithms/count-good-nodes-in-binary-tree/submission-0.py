# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = []
        def dfs(n, max_val):
            nonlocal res
            if not n:
                return
            
            if n.val >= max_val:
                res.append(n.val)
                max_val = n.val

            dfs(n.left, max_val)
            dfs(n.right, max_val)

        dfs(root, root.val)
        return len(res)