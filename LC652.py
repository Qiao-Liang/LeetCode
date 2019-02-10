# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        dic = {}
        res = []

        def recurse(root):
            if not root:
                return '#'

            key = ''.join([str(root.val), recurse(root.left), recurse(root.right)])

            if key in dic:
                if dic[key] == 1:
                    res.append(root)
                    dic[key] = 2
            else:
                dic[key] = 1

            return key

        recurse(root)

        return res

        # dic = {}
        # queue = [root]

        # while len(queue) > 0:
        #     temp = queue.pop(0)
        #     key = tuple([temp.left.val if temp.left is not None else None, temp.val, temp.right.val if temp.right is not None else None])

        #     if key in dic:
        #         dic[key].append(temp)
        #     else:
        #         dic[key] = [temp]

        #     if temp.left:
        #         queue.append(temp.left)

        #     if temp.right:
        #         queue.append(temp.right)

        # return [val[0] for val in dic.values() if len(val) > 1]


sol = Solution()

n0 = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(4)

n0.left = n1
n0.right = n2
n1.left = n3
n2.left = n4
n2.right = n5
n4.left = n6

# n0 = TreeNode(2)
# n1 = TreeNode(2)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(3)

# n0.left = n1
# n0.right = n2
# n1.left = n3
# n2.left = n4

# n0 = TreeNode(0)
# n1 = TreeNode(0)
# n2 = TreeNode(0)
# n3 = TreeNode(0)
# n4 = TreeNode(None)
# n5 = TreeNode(None)
# n6 = TreeNode(0)
# n7 = TreeNode(None)
# n8 = TreeNode(0)

# n0.left = n1
# n0.right = n2
# n1.left = n3
# n1.right = n4
# n2.left = n5
# n2.right = n6
# n6.left = n7
# n6.right = n8

print([node.val for node in sol.findDuplicateSubtrees(n0)])
