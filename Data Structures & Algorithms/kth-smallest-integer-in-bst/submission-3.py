# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative in order DFS

        if root is None:
            return None

        stack=[]
        res=[]
        curr=root

        while curr or stack:

            while curr: # dive left 
                stack.append(curr)
                curr=curr.left
            
            node = stack.pop()
            res.append(node.val)
            if len(res)==k:
                return node.val
            curr=node.right
    
        print(res)










