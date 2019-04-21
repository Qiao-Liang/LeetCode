# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        dic = {}

        def get_depth(node, parent, deepth):
            if not node:
                return

            dic[node.val] = (deepth, parent)
            get_depth(node.left, node, deepth + 1)
            get_depth(node.right, node, deepth + 1)

        get_depth(root, None, 0)
        return dic[x][0] == dic[y][0] and dic[x][1] != dic[y][1]

        # x_deepth = y_deepth = None
        # queue = [root]
        # deepth = 0

        # while queue:
        #     temp_queue = []

        #     for node in queue:
        #         if node.val == x:
        #             x_deepth = deepth

        #         if node.val == y:
        #             y_deepth = deepth

        #         if node.left:
        #             temp_queue.append(node.left)

        #         if node.right:
        #             temp_queue.append(node.right)

        #     if x_deepth != None and y_deepth != None:
        #         return x_deepth == y_deepth

        #     deepth += 1
        #     queue = temp_queue


sol = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
# n5 = TreeNode(5)

n1.left = n2
n1.right = n3
n2.right = n4
# n3.right = n5

print(sol.isCousins(n1, 2, 3))
        