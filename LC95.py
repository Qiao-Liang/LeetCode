# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        memo = {}

        def recurse(srt, end):
            if srt == end:
                return [TreeNode(srt)]
            else:
                if (srt, end) in memo:
                    return memo[(srt, end)]

                res = []

                for val in range(srt, end + 1):
                    left = [None] if val == srt else recurse(srt, val - 1)
                    right = [None] if val == end else recurse(val + 1, end)
                    
                    for l in left:
                        for r in right:
                            node = TreeNode(val)
                            node.left = l
                            node.right = r
                            res.append(node)

                memo[(srt, end)] = res
                return res

        return recurse(1, n)


sol = Solution()
res = sol.generateTrees(3)
print(res)
