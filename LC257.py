# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root:
            paths = []
            output = []
            self.dfs(root, [], paths)

            for path in paths:
                output.append("->".join([str(s) for s in path]))

            return output
        else:
            return []
        
    def dfs(self, root, path, paths):
        if root:
            path.append(root.val)
            
            if root.left or root.right:
                if root.left:
                    self.dfs(root.left, path, paths)
                    path.pop()
                if root.right:
                    self.dfs(root.right, path, paths)
                    path.pop()
            else:
                paths.append(path[:])
