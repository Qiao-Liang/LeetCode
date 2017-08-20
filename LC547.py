class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        circle = set()
        def dfs(std_id):
            for idx, val in enumerate(M[std_id]):
                if val == 1 and idx not in circle:
                    circle.add(idx)
                    dfs(idx)
        
        cir_num = 0
        for idx in range(len(M)):
            if idx not in circle:
                cir_num += 1
                circle.add(idx)
                dfs(idx)
        
        return cir_num


sol = Solution()
M = [[1,1,0], [1,1,0], [0,0,1]]
# M = [[1,1,0], [1,1,1], [0,1,1]]
# M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
count = sol.findCircleNum(M)
