# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []

        def recurse(root):
            if root:
                self.res.append(root.val)
                recurse(root.left)
                recurse(root.right)

        recurse(root)

        return self.res


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

sol = Solution()
print sol.preorderTraversal(n1)
        