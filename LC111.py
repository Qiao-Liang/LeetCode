# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root:
        #     if root.left and root.right:
        #         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        #     else:
        #         return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # else:
        #     return 0
        
        # Below is the BFS solution, which is way faster
        if root:
            depth = 0
            queue = [root]
            
            while len(queue):
                depth += 1
                count = len(queue)
                
                while count > 0:
                    curr = queue.pop(0)
                    if not curr.left and not curr.right:
                        return depth
                    else:
                        if curr.left:
                            queue.append(curr.left)
                        if curr.right:
                            queue.append(curr.right)
                    
                    count -= 1
        else:
            return 0
        