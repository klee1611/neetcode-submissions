# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def dfs(n):
            if not n:
                return
            
            dfs(n.left)
            if len(arr) == k:
                return

            if len(arr) < k:
                arr.append(n.val)

            if len(arr) == k:
                return

            dfs(n.right)
            return

        dfs(root)
        return arr[-1]