# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        curr = root

        while True:
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
            elif val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            else:
                break

        return root


sol = Solution()
root = sol.insertIntoBST(None, 4)
root = sol.insertIntoBST(root, 5)
root = sol.insertIntoBST(root, 3)
root = sol.insertIntoBST(root, 1)
root = sol.insertIntoBST(root, 2)

queue = [root]

while queue:
    temp_queue = []

    print([node.val for node in queue])

    for node in queue:
        if node.left:
            temp_queue.append(node.left)

        if node.right:
            temp_queue.append(node.right)
        
    queue = temp_queue


        