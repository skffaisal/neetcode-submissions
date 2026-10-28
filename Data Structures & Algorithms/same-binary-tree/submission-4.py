# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative DFS

        stack=[(p,q)] # roots of each tree

        while stack:
            node1,node2=stack.pop() # ie right and left nodes

            # same 3 cases 
            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val!=node2.val:
                return False

            # not checking if node1.left or right present , because its already covered in above conditions

            stack.append((node1.right,node2.right))
            stack.append((node1.left,node2.left))

            

        return True # all nodes match

