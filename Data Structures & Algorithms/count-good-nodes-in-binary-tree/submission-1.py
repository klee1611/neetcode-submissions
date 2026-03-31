# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        r = 0
        def dfs(node, max_v):
            if not node:
                return

            nonlocal r
            if node.val >= max_v:
                r += 1
                max_v = node.val

            dfs(node.left, max_v)
            dfs(node.right, max_v)
        dfs(root, root.val)

        return r