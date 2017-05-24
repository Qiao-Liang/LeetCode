# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            l_height = 0
            r_height = 0
            
            if root.left:
                l_height = self.get_height(root.left)
            
            if root.right:
                r_height = self.get_height(root.right)
            
            return abs(l_height - r_height) <= 1
        else:
            return True
        
    
    def get_height(self, root):
        if root:
            return max(self.get_height(root.left), self.get_height(root.right)) + 1
        else:
            return 0
            