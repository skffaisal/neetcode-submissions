# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def depth(root):
            if not root:
                return 0
            
            return 1+max(depth(root.left),depth(root.right))
        
        def dfs(root):
            nonlocal res
            if not root:
                return None
            left=depth(root.left)
            right=depth(root.right)

            res = max(res, left + right)

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
            