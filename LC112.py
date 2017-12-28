# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        self.target = sum
        self.exists = False

        def dfs(node):
            print(node.val)
            if self.exists:
                return
        
            self.target -= node.val

            if node.left or node.right:
                if node.left:
                    dfs(node.left)

                if node.right:
                    dfs(node.right)
            else:
                if self.target == 0:
                    self.exists = True

            self.target += node.val

        dfs(root)
            
        return self.exists


    def hasPathSum2(self, root, sum):
        """
        Recursively check sub trees.

        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        print(root.val)
        if not root:
            return False

        if not root.left and not root.right:
            return sum == root.val
        elif not root.left:
            return self.hasPathSum2(root.right, sum - root.val)
        elif not root.right:
            return self.hasPathSum2(root.left, sum - root.val)
        else:
            return self.hasPathSum2(root.right, sum - root.val) or self.hasPathSum2(root.left, sum - root.val)


        # stack = [root]

        # while stack:
        #     temp = stack[-1]

        #     if temp.left or temp.right:
        #         sum -= temp.val

        #         if temp.right:
        #             stack.append(temp.right)

        #         if temp.left:
        #             stack.append(temp.left)
        #     else:
        #         if sum == temp.val:
        #              return True

        # return False


n1 = TreeNode(5)
n21 = TreeNode(4)
n22 = TreeNode(8)
n31 = TreeNode(11)
n32 = TreeNode(13)
n33 = TreeNode(4)
n41 = TreeNode(7)
n42 = TreeNode(2)
n43 = TreeNode(1)

n1.left = n21
n1.right = n22
n21.left = n31
n22.left = n32
n22.right = n33
n31.left = n41
n31.right = n42
n33.right = n43

# n1 = TreeNode(1)
# n21 = TreeNode(-2)
# n22 = TreeNode(-3)
# n31 = TreeNode(1)
# n32 = TreeNode(3)
# n33 = TreeNode(-2)
# n41 = TreeNode(-1)

# n1.left = n21
# n1.right = n22
# n21.left = n31
# n21.right = n32
# n22.left = n33
# n31.left = n41

# n1 = TreeNode(0)
# n21 = TreeNode(1)
# n22 = TreeNode(1)

# n1.left = n21
# n1.right = n22

sol = Solution()
# print(sol.hasPathSum(n1, 22))
print(sol.hasPathSum(n1, 22))
print(sol.hasPathSum2(n1, 22))
