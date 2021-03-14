# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def count(node, visited):
            if node not in visited:
                visited.add(node)
                res = 1
                
                for nei in g[node]:
                    res += count(nei, visited)
                    
                return res
            else:
                return 0
                
        
        g = defaultdict(list)
        queue = [root]
        
        while queue:
            temp = []
            
            for node in queue:
                if node.left:
                    g[node.val].append(node.left.val)
                    g[node.left.val].append(node.val)
                    temp.append(node.left)
                
                if node.right:
                    g[node.val].append(node.right.val)
                    g[node.right.val].append(node.val)
                    temp.append(node.right)
                    
            queue = temp
        
        nodes = g[x]
        
        while nodes:
            if count(nodes.pop(), set([x])) << 1 > n:
                return True
            
        return False


sol = Solution()
nodes = [None] * 8

for i in range(1, 8):
    nodes[i] = TreeNode(i)

nodes[6].left = nodes[3]
nodes[3].left = nodes[7]
nodes[3].right = nodes[4]
nodes[4].right = nodes[2]
nodes[2].right = nodes[1]
nodes[1].right = nodes[5]

print(sol.btreeGameWinningMove(nodes[6], 7, 3))
