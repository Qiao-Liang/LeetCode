# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.curr_sum = 0
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.curr_sum += node.val
            node.val = self.curr_sum
            dfs(node.left)
            
        dfs(root)
        return root
