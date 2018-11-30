# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        stack = [(root, 0)]
        res = 0

        while stack:
            node, val = stack.pop()
            val = val * 10 + node.val

            if not node.left and not node.right:
                res += val
            else:
                if node.left:
                    stack.append((node.left, val))

                if node.right:
                    stack.append((node.right, val))

        return res
            

        # self.nums = []

        # def dfs(root, temp):
        #     temp = temp * 10 + root.val

        #     if not root.left and not root.right:
        #         self.nums.append(temp)

        #     if root.left:
        #         dfs(root.left, temp)
            
        #     if root.right:
        #         dfs(root.right, temp)

        # dfs(root, 0)

        # return sum(self.nums)


n0 = TreeNode(0)
n1 = TreeNode(1)
n4 = TreeNode(4)
n5 = TreeNode(5)
n9 = TreeNode(9)

n4.left = n9
n4.right = n0
n9.left = n5
n9.right = n1

sol = Solution()
print sol.sumNumbers(n4)
        