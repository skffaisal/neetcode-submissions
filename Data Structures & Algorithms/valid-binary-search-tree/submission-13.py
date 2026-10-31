# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,low,high):
            if root is None:
                return True
            curr = low<root.val<high                  
            return curr and dfs(root.left,low=low,high=root.val) and  dfs(root.right,low=root.val,high=high)
            
        return dfs(root,float('-inf'),float('inf'))



#   my_piece              dfs(root.left        dfs(root.right       result
        # 2                      true                      true        true
        # 1                      false                     false        false 
