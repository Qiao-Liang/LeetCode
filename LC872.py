# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root, res):
            if not root.left and not root.right:
                res.append(root.val)

            if root.left:
                dfs(root.left, res)

            if root.right:
                dfs(root.right, res)

        res1 = []
        res2 = []
        dfs(root1, res1)
        dfs(root2, res2)
        return res1 == res2


sol = Solution()
n00 = TreeNode(1)
n01 = TreeNode(2)
n02 = TreeNode(3)
n03 = TreeNode(4)
n04 = TreeNode(5)

n00.left = n01
n00.right = n02
n02.left = n03
n02.right = n04

n10 = TreeNode(1)
n11 = TreeNode(0)
n12 = TreeNode(2)
n13 = TreeNode(4)
n14 = TreeNode(6)

n10.left = n11
n10.right = n14
n11.left = n12
n11.right = n13

print(sol.leafSimilar(n00, n10))
