# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = 0
        queue = [root]

        while queue:
            res += len(queue)
            temp_queue = []

            for node in queue:
                if node.left:
                    temp_queue.append(node.left)
                
                if node.right:
                    temp_queue.append(node.right)

            queue = temp_queue

        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

sol = Solution()
print(sol.countNodes(node1))
