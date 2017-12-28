# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1

        min_val = root.val
        sec_min_val = -1
        queue = [root]

        while queue:
            temp = queue.pop(0)

            if sec_min_val == -1:
                if temp.val > min_val:
                    sec_min_val = temp.val
            else:
                if temp.val < min_val:
                    sec_min_val = min_val
                    min_val = temp.val
                elif sec_min_val > temp.val > min_val:
                    sec_min_val = temp.val

            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        return sec_min_val


# n1 = TreeNode(2)
# n21 = TreeNode(2)
# n22 = TreeNode(5)
# n31 = TreeNode(5)
# n32 = TreeNode(7)

n1 = TreeNode(2)
n21 = TreeNode(2)
n22 = TreeNode(2)

n1.left = n21
n1.right = n22
# n22.left = n31
# n22.right = n32

sol = Solution()
print(sol.findSecondMinimumValue(n1))
