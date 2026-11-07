# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(root,l,h):
            if not root:
                return True

            return ( l<root.val<h and 
            bst(root.left,l,root.val) and 
            bst(root.right,root.val,h) )



        return bst(root,float('-inf'),float('inf'))