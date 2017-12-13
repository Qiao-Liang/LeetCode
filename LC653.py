# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = [root]

        while queue:
            curr = queue.pop(0)
            temp = root
            trgt = k - curr.val

            while temp:
                if trgt > temp.val:
                    temp = temp.right
                elif trgt < temp.val:
                    temp = temp.left
                else:
                    if temp == curr:
                        break
                    else:
                        return True

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return False


n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6

sol = Solution()
print(sol.findTarget(n1, 10))
