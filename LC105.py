# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            root_val = preorder.pop(0)
            root_idx = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = self.buildTree(preorder, inorder[:root_idx])
            root.right = self.buildTree(preorder, inorder[root_idx + 1:])

            return root


sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = sol.buildTree(preorder, inorder)
print root
