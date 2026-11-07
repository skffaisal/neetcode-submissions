# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # postorder, the nodes gets processed if its visited 2nd time
        stack=[root]
        visit=[False]
        res=[]

        #edge case:
        if not root:
            return []

        while stack:            
            node=stack.pop()
            visited=visit.pop()

            if node and visited:# if node is not None and its previously visited
                res.append(node.val)
            else:
                # put it back and mark as visited, so next visist it it be processed
                stack.append(node)
                visit.append(True)

                # now add the children, since left needs to be processed first, put right in the stack
                if node.right:
                    stack.append(node.right)
                    visit.append(False) # ie first time so false
                
                if node.left:
                    stack.append(node.left)
                    visit.append(False)

        return res


        