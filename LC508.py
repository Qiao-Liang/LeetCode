# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        count = defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
            
            temp = node.val + dfs(node.left) + dfs(node.right)
            count[temp] += 1
            return temp
        
        dfs(root)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]

