# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node):
            if not node:
                return (None, 0)
            
            lv, lc = dfs(node.left)
            rv, rc = dfs(node.right)
            temp = max_temp = 0
            
            if lv == node.val:
                lc += 1
                temp += lc
                max_temp = max(max_temp, lc)
                
            if rv == node.val:
                rc += 1
                temp += rc
                max_temp = max(max_temp, rc)
            
            self.res = max(self.res, temp)
            return (node.val, max_temp)
            
        dfs(root)
        return self.res

    # def longestUnivaluePath(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     res = 0

    #     def dfs(node, length):
    #         nonlocal res

    #         if node.left:
    #             res = max(res, length)
    #             dfs(node.left, length + 1 if node.val == node.left.val else 1)

    #         if node.right:
    #             res = max(res, length)
    #             dfs(node.right, length + 1 if node.val == node.right.val else 1)

    #     dfs(root, 1)
    #     return res


sol = Solution()
n0 = TreeNode(5)
n1 = TreeNode(4)
n2 = TreeNode(5)
n3 = TreeNode(1)
n4 = TreeNode(1)
n5 = TreeNode(5)

n0.left = n1
n0.right = n2
n1.left = n3
n1.right = n4
n2.right = n5

print(sol.longestUnivaluePath(n0))
        