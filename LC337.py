# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        rob_dict = {}
        not_rob_dict = {}

        def recurse(root, can_rob, idx):
            if not root:
                return 0

            left_idx = idx * 2 + 1
            right_idx = left_idx + 1

            if can_rob:
                if idx not in rob_dict:
                    rob_dict[idx] = max(recurse(root.left, False, left_idx) + recurse(root.right, False, right_idx) + root.val, recurse(root.left, True, left_idx) + recurse(root.right, True, right_idx))

                return rob_dict[idx]
            else:
                if idx not in not_rob_dict:
                    not_rob_dict[idx] = recurse(root.left, True, left_idx) + recurse(root.right, True, right_idx)

                return not_rob_dict[idx]

        return max(recurse(root, True, 0), recurse(root, False, 0))


node0 = TreeNode(3)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(3)
node4 = TreeNode(1)

node0.left = node1
node0.right = node2
node1.right = node3
node2.right = node4

sol = Solution()
print sol.rob(node0)
