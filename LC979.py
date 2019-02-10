# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            self.res = abs(left) + abs(right)
            return root.val + left + right - 1
        
        dfs(root)
        return self.res

        # if not root:
        #     return 0

        # self.res = 0

        # def dfs(node):
        #     temp_left = temp_right = 0

        #     if node.left:
        #         dfs(node.left)
        #         temp_left = abs(node.left.val - 1)
        #         node.val = node.val + node.left.val - 1
            
        #     if node.right:
        #         dfs(node.right)
        #         temp_right = abs(node.right.val - 1)
        #         node.val = node.val + node.right.val - 1

        #     self.res += temp_left + temp_right

        # dfs(root)
        # return self.res


        # res = 0
        # dic = {}

        # def dfs_distance(parent, node):
        #     nonlocal dic

        #     if not node:
        #         return 0

        #     if node.val > 1:
        #         dic[node] = 0
        #         dfs_distance(node, node.left)
        #         dfs_distance(node, node.right)
        #     elif node.val == 0:
        #         dic[node] = min(dfs_distance(node, node.left), dfs_distance(node, node.right), dic[parent] if parent else float('inf')) + 1

        #     return dic[node]

        # def dfs_min(parent, child):
        #     nonlocal dic, res

        #     if child.val == 0:
        #         res += min(dic[child], (dic[parent] + 1 if parent else float('inf')))

        #     if child.left:
        #         dfs_min(child, child.left)

        #     if child.right:
        #         dfs_min(child, child.right)

        # dfs_distance(None, root)
        # dfs_min(None, root)

        # return res


sol = Solution()

n0 = TreeNode(0)
n1 = TreeNode(3)
n2 = TreeNode(0)

n0.left = n1
n0.right = n2

print(sol.distributeCoins(n0))
        