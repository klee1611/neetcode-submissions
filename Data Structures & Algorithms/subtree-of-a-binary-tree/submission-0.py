# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(n1, n2):
            if not n1 and not n2:
                return True
            if not n1:
                return False
            if not n2:
                return False
            if n1.val != n2.val:
                return False
            return same_tree(n1.right, n2.right) and same_tree(n1.left, n2.left)

        def find_subroot(n1, n2):
            if not n1 and not n2:
                return True
            if not n1:
                return False
            if not n2:
                return True

            if n1.val == n2.val:
                if same_tree(n1, n2):
                    return True
            
            return find_subroot(n1.left, n2) or find_subroot(n1.right, n2)

        return find_subroot(root, subRoot)
