# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        r = True
        def dfs(node):
            l_max, l_min = dfs(node.left) if node.left else (float('-inf'), float('inf'))
            r_max, r_min = dfs(node.right) if node.right else (float('-inf'), float('inf'))

            nonlocal r
            if l_max >= node.val or r_min <= node.val:
                r = False
            return max(l_max, r_max, node.val), min(l_min, r_min, node.val)
        dfs(root)
        return r
                
