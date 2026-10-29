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

        # Both targets are smaller → go left.
        if p.val < root.val and q.val <root.val: 
             return self.lowestCommonAncestor(root.left,p,q)

        # Both targets are greater → go right.
        if p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right,p,q) 
        
        # The current node is p or q
        if p.val==root.val or q.val==root.val: # becasue a node counts as its own ancestor
            return root

        # Otherwise, the targets must be on opposite sides
        if p.val < root.val and q.val > root.val:
            return root

        if p.val > root.val and q.val < root.val:
            return root
        

