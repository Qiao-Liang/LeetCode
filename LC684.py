from collections import defaultdict

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dis_set = {}
        ranks = defaultdict(int)
        res = None
        
        def find(x):
            if x != dis_set[x]:
                dis_set[x] = find(dis_set[x])
                
            return dis_set[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            
            if ranks[px] > ranks[py]:
                dis_set[py] = px
                ranks[px] += 1
            else:
                dis_set[px] = py
                ranks[py] += 1
                
            return px == py
                
        for x, y in edges:
            if x not in dis_set:
                dis_set[x] = x
                
            if y not in dis_set:
                dis_set[y] = y
            
            if union(x, y):
                res = [x, y]
        
        return res
