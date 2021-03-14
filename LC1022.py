# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root) -> int:
        self.res = 0
        
        def dfs(node, path):
            path = (path << 1) + node.val
            
            if not node.left and not node.right:
                self.res += path
            else:
                if node.left:
                    dfs(node.left, path)
                    
                if node.right:
                    dfs(node.right, path)
        
        dfs(root, 0)
        return self.res

