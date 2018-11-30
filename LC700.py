# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root

        return None


node0 = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(3)

node0.left = node1
node0.right = node2
node1.left = node3
node1.right = node4

sol = Solution()
temp = sol.searchBST(node0, 2)
print temp
