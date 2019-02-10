# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        temp = []

        queue = [(root, 0, 0)]
        # v_offset = 0
        # h_offset = 0

        while queue:
            elem = queue.pop(0)

            if elem[1] in dic:
                dic[elem[1]].append((elem[0].val, elem[2]))
            else:
                dic[elem[1]] = [(elem[0].val, elem[2])]
            # temp.append((elem[0].val, elem[1], elem[2]))

            if elem[0].left:
                queue.append((elem[0].left, elem[1] - 1, elem[2] - 1))
            
            if elem[0].right:
                queue.append((elem[0].right, elem[1] + 1, elem[2] - 1))

        return [[] temp.sort(lambda n: n[1])]

        