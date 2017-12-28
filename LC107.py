# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = [root]
        result = [[root.val]]
        temp = []

        while queue:
            node = queue.pop(0)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            
            if not queue:
                if temp:
                    result.append([n.val for n in temp])
                    queue = temp
                    temp = []
                else:
                    return result[::-1]
        

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
print(sol.levelOrderBottom(n1))
