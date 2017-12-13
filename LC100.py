# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            p_queue = [p]
            q_queue = [q]

            while p_queue and q_queue:
                temp_p = p_queue.pop(0)
                temp_q = q_queue.pop(0)

                if temp_p.val != temp_q.val:
                    return False

                if temp_p.left and temp_q.left:
                    if temp_p.left.val == temp_q.left.val:
                        p_queue.append(temp_p.left)
                        q_queue.append(temp_q.left)
                    else:
                        return False
                elif not temp_p.left and not temp_q.left:
                    pass
                else:
                    return False

                if temp_p.right and temp_q.right:
                    if temp_p.right.val == temp_q.right.val:
                        p_queue.append(temp_p.right)
                        q_queue.append(temp_q.right)
                    else:
                        return False
                elif not temp_p.right and not temp_q.right:
                    pass
                else:
                    return False

            if p_queue or q_queue:
                return False
            else:
                return True
        elif not p and not q:
            return True
        else:
            return False


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
b1 = TreeNode(1)
b2 = TreeNode(2)
b3 = TreeNode(3)

a1.left = a2
a1.right = a3
a3.left = a4
b1.left = b2
b1.right = b3

sol = Solution()
# print(sol.isSameTree(a1, b1))
print(sol.isSameTree(None, None))
        