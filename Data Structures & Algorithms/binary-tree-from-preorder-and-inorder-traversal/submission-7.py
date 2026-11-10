# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map={}
        for i in range(len(inorder)):
            inorder_map[inorder[i]]=i

        
        self.pre_index=0
        def dfs(l,r):
            if l>r:
                return None
            root=TreeNode(preorder[self.pre_index])            
            root_index=inorder_map[preorder[self.pre_index]]
            self.pre_index+=1
            root.left=dfs(l,root_index-1)
            root.right=dfs(root_index+1,r)

            return root
        return dfs(0,len(inorder)-1)


