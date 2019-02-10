# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            # def check_height(root):
            #     if root:
            #         l_balanced, l_height = check_height(root.left)
            #         r_balanced, r_height = check_height(root.right)

            #         return (abs(l_height - r_height) < 2 if l_balanced and r_balanced else False), max(l_height, r_height) + 1
            #     else:
            #         return True, 0

            # return check_height(root)[0]

            def check_height(root):
                if root:
                    l_height = check_height(root.left)
                    r_height = check_height(root.right)

                    return -1 if l_height == -1 or r_height == -1 or abs(l_height - r_height) > 1 else max(l_height, r_height) + 1
                else:
                    return 0
            
            return check_height(root) != -1
        else:
            return True


sol = Solution()

# n0 = TreeNode(3)
# n1 = TreeNode(9)
# n2 = TreeNode(20)
# n3 = TreeNode(15)
# n4 = TreeNode(7)

# n0.left = n1
# n0.right = n2
# n2.left = n3
# n2.right = n4

n0 = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(3)
n5 = TreeNode(4)
n6 = TreeNode(4)

n0.left = n1
n0.right = n2
n1.left = n3
n2.right = n4
n3.left = n5
n4.right = n6

print(sol.isBalanced(n0))
            