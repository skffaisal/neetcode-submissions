class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Get the maximum gain from left and right subtrees.
            # If the gain is negative, we are better off ignoring it (taking 0).
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Price of the path starting at this node and splitting into both children
            current_path_sum = node.val + left + right
            
            # Update our global maximum result
            self.res = max(self.res, current_path_sum)
            
            # Return the maximum gain if the parent continues down this branch
            return node.val + max(left, right)
        
        # Don't forget to kick off the DFS!
        dfs(root) 
        return self.res
