# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # lowestCommonAncestor(root.left,p,q)  lowestCommonAncestor(root.right,p,q)
        
        if root is None:
            return None

        if p.val < root.val and q.val <root.val: # Both targets are smaller → go left.
             return self.lowestCommonAncestor(root.left,p,q)

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q) # Both targets are greater → go right.
        
        return root 
