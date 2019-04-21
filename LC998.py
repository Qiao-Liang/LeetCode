# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def deconstruct(node):
            if not node:
                return []

            return deconstruct(node.left) + [node.val] + deconstruct(node.right)

        def construct(node_list):
            if not node_list:
                return None

            max_idx = 0
            max_val = node_list[0]

            for idx, val in enumerate(node_list):
                if val > max_val:
                    max_val = val
                    max_idx = idx

            root = TreeNode(max_val)
            root.left = construct(node_list[:max_idx])
            root.right = construct(node_list[max_idx + 1:])

            return root

        temp_list = deconstruct(root)
        temp_list.append(val)

        return construct(temp_list)
        