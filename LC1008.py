# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def recurse(vals):
            if not vals:
                return None

            root_val = vals.pop(0)
            root = TreeNode(root_val)
            idx = 0
            len_vals = len(vals)

            while idx < len_vals and vals[idx] < root_val:
                idx += 1

            root.left = recurse(vals[:idx])
            root.right = recurse(vals[idx:])
            return root

        return recurse(preorder)
