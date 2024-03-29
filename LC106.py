# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_val = postorder.pop()
            root = TreeNode(root_val)
            index = inorder.index(root_val)
            root.right = self.buildTree(inorder[index + 1:], postorder)
            root.left = self.buildTree(inorder[:index], postorder)
            
            return root


sol = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
temp = sol.buildTree(inorder, postorder)
print temp   
        