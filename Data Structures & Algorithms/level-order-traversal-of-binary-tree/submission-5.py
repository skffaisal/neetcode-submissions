# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: # Iterative DFS

        stack=[(root,0)]# 0 is the depth
        res=[]
        if root is None:
            return res
        while stack:
            node,depth=stack.pop()
            # print(node.val,depth)

            if len(res)==depth:
                res.append([])
            res[depth].append(node.val)

            if node.right:
                stack.append((node.right,depth+1))
            if node.left:
                stack.append((node.left,depth+1))
            

        return res
        