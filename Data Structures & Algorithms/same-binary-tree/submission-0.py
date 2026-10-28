# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None: # both are same 
            return True
        if p is None or q is None: # if either one is different
            return False

        # smaller input: isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        return p.val ==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)