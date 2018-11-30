# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        self.accu_sum = 0
        def recurse(root):
            if root.right:
                recurse(root.right)
            
            root.val += self.accu_sum
            self.accu_sum = root.val

            if root.left:
                recurse(root.left)

        # def recurse(root, res):
            # if root.right:
            #     res = convert(root.right, res)
            # root.val += res
            # res = root.val
            # if root.left:
            #     res = convert(root.left, res)
            # return res

        recurse(root)

        return root


        # array = []

        # def recurse(root, array):            
        #     if root.left:
        #         recurse(root.left, array)
            
        #     array.append(root.val)

        #     if root.right:
        #         recurse(root.right, array)

        # self.idx = 0

        # def restore(root, array):
        #     if root.left:
        #         restore(root.left, array)

        #     root.val = array[self.idx]
        #     self.idx += 1

        #     if root.right:
        #         restore(root.right, array)

        # recurse(root, array)

        # for idx in xrange(len(array) - 2, -1, -1):
        #     array[idx] += array[idx + 1]

        # restore(root, array)

        # return root


node0 = TreeNode(5)
node1 = TreeNode(2)
node2 = TreeNode(13)

node0.left = node1
node0.right = node2

sol = Solution()
temp = sol.convertBST(node0)
print temp
