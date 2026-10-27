# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # # my_piece           # below                                            # result
        # root.val              maxDepth(root.left), maxDepth(root.left)               
        #     1                          0          , 2                                  3

        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
