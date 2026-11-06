# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left=self.deleteNode(root.left,key)
        elif key >root.val:
            root.right=self.deleteNode(root.right,key)

        else:
            # handling if only children are present 
            if not root.left:
                return root.right
        
            if not root.right:
                return root.left

            # handling if both childrens are there,
            sucessor=root.right

            # need to find the smallest eleemnt in this right subtree
            while sucessor.left:
                if not sucessor.left:
                    break
                sucessor=sucessor.left
        
            root.val=sucessor.val

            root.right=self.deleteNode(root.right,sucessor.val)

        return root

