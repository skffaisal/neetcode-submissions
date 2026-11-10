# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        self.res=""
        def dfs(root):
            if root is None:
                self.res+='N|'
                return None
            self.res+=str(root.val) + '|'
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        # print(self.res)
        return self.res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        preorder=data.split('|')
        # print(preorder)
        self.i=0
        def dfs():
            if preorder[self.i].isdigit():

                root=TreeNode(int(preorder[self.i]))
                self.i+=1
            elif preorder[self.i] == 'N':
                self.i+=1
                return None


            root.left=dfs()
            root.right=dfs()

            return root
        return dfs()

