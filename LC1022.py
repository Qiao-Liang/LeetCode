# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, val):
            if not node:
                return 0
            
            val = val << 1 + node.val

            if not node.left and not node.right:
                return val

            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)
