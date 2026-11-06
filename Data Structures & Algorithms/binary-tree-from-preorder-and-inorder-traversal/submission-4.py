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

        def helper(pre_start,pre_end,in_start,in_end):
            if pre_start > pre_end: # empty list
                return None

            root= TreeNode(preorder[pre_start]) # same as preorder[0], but since here we are passing the boundaries, it will change

            root_index=inorder_map[preorder[pre_start]] # root_index of the inorder, this is undesrtood right? 

            # ie how do i get how many elements in the left subtree, in inorder
            left_size = root_index - in_start

            # here i need to pass preorder and inorder boundaries of left subtree
            # inorder[:root_index] -> in_start,root_index-1
            # preorder[1,root_index+1] -> pre_start+1, pre_start + left_size
            root.left = helper(pre_start+1,pre_start + left_size,in_start,root_index-1)
            
            # here i need to pass preorder and inorder boundaries for right subtree
            # inorder[root_index+1:] -> root_index+1,in_end
            # preorder[root_index+1:] -> pre_start+1+left_size, pre_end
            root.right=helper(pre_start+1+left_size, pre_end,root_index+1,in_end)

            return root 

        return helper(0,len(preorder)-1,0,len(inorder)-1)

            

