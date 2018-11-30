from sys import maxint

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sorted_tree = []

        def recurse(root):
            if root.left:
                recurse(root.left)

            self.sorted_tree.append(root.val)

            if root.right:
                recurse(root.right)

        recurse(root)
        min_diff = maxint

        for idx in xrange(len(self.sorted_tree) - 1):
            min_diff = min(min_diff, self.sorted_tree[idx + 1] - self.sorted_tree[idx])

        return min_diff


        # queue = [root]
        # min_diff = root.val

        # while len(queue) > 0:
        #     temp_queue = []

        #     for node in queue:
        #         if node.left:
        #             min_diff = min(min_diff, abs(node.val - node.left.val))
        #             temp_queue.append(node.left)
                
        #         if node.right:
        #             min_diff = min(min_diff, abs(node.val - node.right.val))
        #             temp_queue.append(node.right)

        # return min_diff


sol = Solution()
node0 = TreeNode(1)
node1 = TreeNode(2)
# node2 = TreeNode(3)

node0.right = node1
# node1.left = node2

print sol.getMinimumDifference(node0)
