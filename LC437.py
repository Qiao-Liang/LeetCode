# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0

        def do_recurse(root, sum, remain):
            if root.left:
                recurse(root.left, sum, remain)
            
            if root.right:
                recurse(root.right, sum, remain)

        def recurse(root, sum, remain):
            if not root:
                return
            
            if remain == root.val:
                self.count += 1
                remain = sum
            else:
                remain -= root.val

            do_recurse(root, sum, remain)
            do_recurse(root, sum, sum)

        recurse(root, sum, sum)

        return self.count


sol = Solution()
# temp_nodes  = [10,5,-3,3,2,None,11,3,-2,None,1]
# temp_nodes = [5,4,8,11,None,13,4,7,2,None,None,5,1]
# temp_nodes = [-2, None, -3]
temp_nodes = [1,None,2,None,3,None,4,None,5]
nodes = [TreeNode(val) if val else None for val in temp_nodes]

for idx in xrange(len(nodes)):
    if nodes[idx] and idx * 2 + 1 < len(nodes):
        nodes[idx].left = nodes[idx * 2 + 1]
    
    if nodes[idx] and idx * 2 + 2 < len(nodes):
        nodes[idx].right = nodes[idx * 2 + 2]

print sol.pathSum(nodes[0], 3)

