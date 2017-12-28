# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        self.result = None

        def dfs(node):
            if self.result or not node:
                return

            dfs(node.left)

            self.count -= 1
            if self.count == 0:
                self.result = node.val

            dfs(node.right)

        dfs(root)

        return self.result
        

n1 = TreeNode(15)
n21 = TreeNode(7)
n22 = TreeNode(20)
n31 = TreeNode(3)
n32 = TreeNode(9)

n1.left = n21
n1.right = n22
n21.left = n31
n21.right = n32

sol = Solution()
print(sol.kthSmallest(n1, 3))
