# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = [root]

        while queue:
            values = [n.val if n else None for n in queue]

            if values != values[::-1]:
                return False

            queue = [c for n in queue if n for c in [n.left, n.right]]

        return True

# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if not root:
#             return True

#         queue = [root]
#         temp_queue = []
#         chk_pnt = 2

#         while queue:
#             temp = queue.pop(0)

#             if temp:
#                 if temp.left:
#                     temp_queue.append(temp.left)
#                 else:
#                     temp_queue.append(None)
                
#                 if temp.right:
#                     temp_queue.append(temp.right)
#                 else:
#                     temp_queue.append(None)
#             else:
#                 temp_queue.extend([None, None])

#             if not queue:
#                 l = 0
#                 r = len(temp_queue) - 1
#                 end = True

#                 while l < r:
#                     left = temp_queue[l]
#                     right = temp_queue[r]
#                     if left and right:
#                         end = False
#                         if left.val != right.val:
#                             return False
#                     elif not left and not right:
#                         pass
#                     else:
#                         return False

#                     l += 1
#                     r -= 1
                
#                 if end:
#                     break
#                 else:
#                     queue = temp_queue
#                     temp_queue = []

#         return True


n1 = TreeNode(1)
n21 = TreeNode(2)
n22 = TreeNode(2)
n31 = TreeNode(3)
n32 = TreeNode(4)
n33 = TreeNode(4)
n34 = TreeNode(3)

n1.left = n21
n1.right = n22
# n21.left = n31
# n21.right = n32
# n22.left = n33
# n22.right = n34
n21.left = n31
n22.right = n34
n31.left = n32
n34.right = n33
# n34.left = n33

sol = Solution()
print(sol.isSymmetric(n1))
