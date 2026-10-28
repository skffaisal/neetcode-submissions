# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    
        # since iam not traversing subRoot
        stack=[root]

        while stack:
            node=stack.pop()

            if node.val==subRoot.val and self.sameTree(node,subRoot):
                return True
        
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
        return False


    # return root.val==subroot.val and self.sameTree(root,Subroot), from the table  

    def sameTree(self,p,q)->bool: # helper function

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)



