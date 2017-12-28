# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [root]
        result = 0

        while queue:
            temp = queue.pop(0)
            
            if temp.left:
                if not temp.left.left and not temp.left.right:
                    result += temp.left.val
                
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return result


n1 = TreeNode(3)
n21 = TreeNode(9)
n22 = TreeNode(20)
n31 = TreeNode(15)
n32 = TreeNode(7)

n1.left = n21
n1.right = n22
n22.left = n31
n22.right = n32

sol = Solution()
print(sol.sumOfLeftLeaves(None))
        