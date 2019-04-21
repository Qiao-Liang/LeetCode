# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        head = TreeNode(-1)
        self.curr = head

        def recurse(root):
            if root.left:
                recurse(root.left)

            root.left = None
            self.curr.right = root
            self.curr = root

            if root.right:
                recurse(root.right)

        recurse(root)

        return head.right

        # self.res = self.last = None
        
        # def dfs(node):
        #     if not node:
        #         return None
            
        #     dfs(node.left)
            
        #     if not self.res:
        #         self.res = node
                
        #     if self.last:
        #         self.last.right = node
            
        #     node.left = None
        #     self.last = node
        #     dfs(node.right)
            
        # dfs(root)
        # return self.res


node0 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
node6 = TreeNode(7)
node7 = TreeNode(8)
node8 = TreeNode(9)

node4.left = node2
node4.right = node5
node2.left = node1
node2.right = node3
node5.right = node7
node1.left = node0
node7.left = node6
node7.right = node8

# node0 = TreeNode(379)
# node1 = TreeNode(826)
# node0.left = node1

sol = Solution()
temp = sol.increasingBST(node4)

print(temp)
