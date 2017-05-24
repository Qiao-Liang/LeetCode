# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p > q:
            p, q = q, p
        
        if root.left.val == p.val and root.right.val == q.val:
            return root.val
        
        if p.right.val == q.val:
            return p.val
            
        if q.left.val == p.val:
            return q.val
        
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        