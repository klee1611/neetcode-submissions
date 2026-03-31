# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque()
        q.append(root)
        levels = []
        while q:
            level = []
            for i in range(len(q)):
                n = q.popleft()
                if not n:
                    continue
                level.append(n.val)
                q.append(n.left)
                q.append(n.right)
            if level:
                levels.append(level)
        return levels
        