# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total_tilt = 0

        def recurse(root):
            if not root:
                return 0

            # if not root.left and not root.right:
            #     return root.val

            left_sum = recurse(root.left)
            right_sum = recurse(root.right)

            self.total_tilt += abs(left_sum - right_sum)

            return root.val + left_sum + right_sum

        recurse(root)

        return self.total_tilt


node0 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)

node0.left = node1
node0.right = node2
node1.left = node3
node2.left = node4

sol = Solution()
print sol.findTilt(node0)
        