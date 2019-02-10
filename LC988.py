# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.res = None
        base = ord('a')

        def dfs(node, temp):
            if not node:
                return
            
            temp.append(node.val)

            if not node.left and not node.right:    
                rev_temp = temp[::-1]

                if not self.res or rev_temp < self.res:
                    self.res = rev_temp
            else:
                temp.append(node.val)
                dfs(node.left, temp)
                dfs(node.right, temp)
            
            temp.pop()

        dfs(root, [])
        return ''.join(map(lambda n: chr(n + base), self.res))


sol = Solution()
n0 = TreeNode(25)
n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(1)
n4 = TreeNode(3)
n5 = TreeNode(0)
n6 = TreeNode(2)

n0.left = n1
n0.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
# n0 = TreeNode(0)
# n1 = TreeNode(1)

# n0.right = n1

print(sol.smallestFromLeaf(n0))


        # res = []
        # base = ord('a')

        # while True:
        #     res.append(root.val)

        #     if not root.left and not root.right:
        #         break
        #     elif root.left and not root.right:
        #         root = root.left
        #     elif root.right and not root.left:
        #         root = 
            

        
                    
        