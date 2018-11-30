# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        self.in_order = []

        def recurse(root):
            if root.left:
                recurse(root.left)
            
            self.in_order.append(root.val)

            if root.right:
                recurse(root.right)

        recurse(root)

        idx = 1
        len_order = len(self.in_order)

        while idx < len_order:
            if self.in_order[idx - 1] >= self.in_order[idx]:
                return False
            
            idx += 1

        return True


        # if not root:
        #     return True

        # if root.left and root.left.val >= root.val or root.right and root.right.val <= root.val:
        #     return False
        # else:
        #     return self.isValidBST(root.left) and self.isValidBST(root.right)


# n1 = TreeNode(1)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
# n6 = TreeNode(6)

# n5.left = n1
# n5.right = n4
# n4.left = n3
# n4.right = n6

n10 = TreeNode(10)
n5 = TreeNode(5)
n15 = TreeNode(15)
n6 = TreeNode(6)
n20 = TreeNode(20)

n10.left = n5
n10.right = n15
n15.left = n6
n15.right = n20

sol = Solution()
print sol.isValidBST(n10)
        