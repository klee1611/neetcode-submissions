# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        inorder_map = {val: index for index, val in enumerate(inorder)}
        
        pre_index = 0
        def dfs(l, r):
            if l > r:
                return None
            
            nonlocal pre_index
            val = preorder[pre_index]
            pre_index +=1

            j = inorder_map[val]
            node = TreeNode(val)
            node.left = dfs(l, j-1)
            node.right = dfs(j+1, r)

            return node
        return dfs(0, len(preorder)-1)