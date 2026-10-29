class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # iteration

        curr=root

        while curr:
            
            # Both targets are smaller → go left.
            if p.val < curr.val and q.val <curr.val: 
                curr=curr.left

            # Both targets are greater → go right.
            elif p.val > curr.val and q.val > curr.val: 
                curr=curr.right
                
            # The current node is p or q
            elif p.val==curr.val or q.val==curr.val:
                return curr

            # Otherwise, the targets must be on opposite sides
            elif  (p.val < curr.val and q.val > curr.val) or (p.val > curr.val and q.val < curr.val):
                return curr
            