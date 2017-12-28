# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        temp_queue = []
        last = root.val

        while True:
            temp = queue.pop(0)

            if temp.left:
                temp_queue.append(temp.left)
            if temp.right:
                temp_queue.append(temp.right)

            if not queue:
                if temp_queue:
                    last = temp_queue[0].val
                    queue = temp_queue
                    temp_queue = []
                else:
                    return last


n1 = TreeNode(1)
n21 = TreeNode(2)
n22 = TreeNode(3)
n31 = TreeNode(4)
n32 = TreeNode(5)
n33 = TreeNode(6)
n41 = TreeNode(7)

n1.left = n21
n1.right = n22
n21.left = n31
n22.left = n32
n22.right = n33
n32.left = n41

sol = Solution()
print(sol.findBottomLeftValue(n1))
