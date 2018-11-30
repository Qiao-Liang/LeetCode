# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        queue = [root]
        res = []

        while queue:
            res.append(queue[-1].val)

            temp_queue = []

            for node in queue:
                if node.left:
                    temp_queue.append(node.left)

                if node.right:
                    temp_queue.append(node.right)

            queue = temp_queue

        return res


n0 = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)

n0.left = n1
n0.right = n2
n1.right = n4
n2.right = n3

sol = Solution()
print sol.rightSideView(n0)
