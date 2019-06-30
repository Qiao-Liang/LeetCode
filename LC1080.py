# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def recurse(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            l = recurse(node.left, curr_sum)
            r = recurse(node.right, curr_sum)
            
            if l + curr_sum < limit:
                node.left = None
                
            if r + curr_sum < limit:
                node.right = None
            
            return max(l, r) + node.val
        
        res = recurse(root, 0)
        return root if res >= limit else None
