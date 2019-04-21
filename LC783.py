# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.res = root.val
        self.last_val = 0

        def dfs(node):
            if node.left:
                dfs(node.left)

            self.res = min(self.res, node.val - self.last_val)
            self.last_val = node.val

            if node.right:
                dfs(node.right)

        dfs(root)
        return self.res
        