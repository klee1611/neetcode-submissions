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

        q = [root]
        levels = []
        while q:
            level = []
            q_next = []
            for i in range(len(q)):
                if not q[i]:
                    continue
                level.append(q[i].val)
                q_next.append(q[i].left)
                q_next.append(q[i].right)
            q = q_next
            if level:
                levels.append(level)
        return levels
        