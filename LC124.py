# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = root.val
        
        def recurse(node):
            if not node:
                return 0
            
            left = recurse(node.left)
            right = recurse(node.right)
            
            self.res = max(self.res, node.val, node.val + left + right, node.val + left, node.val + right)
            return max(node.val, node.val + max(left, right))
        
        recurse(root)
        return self.res
        
#         self.res = 0
#         graph = defaultdict(set)
#         queue = [root]
            
#         for node in queue:
#             if node.left:
#                 queue.append(node.left)
#                 graph[node].add(node.left)
#                 graph[node.left].add(node)

#             if node.right:
#                 queue.append(node.right)
#                 graph[node].add(node.right)
#                 graph[node.right].add(node)
        
#         def recurse(node, visited, temp_sum):
#             for nei in graph[node]:
#                 if nei not in visited:
#                     visited.add(nei)
#                     temp_sum += nei.val
#                     self.res = max(self.res, temp_sum)
#                     recurse(nei, visited, temp_sum)
                    
#         for node in graph.keys():
#             recurse(node, set([node]), node.val)
        
#         return self.res
