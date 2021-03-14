from collections import defaultdict

class Solution:
    def queensAttacktheKing(self, queens, king):
        res = []
        queen_dic = defaultdict(set)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
        borders = [king] * 8
        go_on = True
        
        for r, c in queens:
            queen_dic[r].add(c)
        
        while go_on:
            go_on = False
            
            for i in range(8):
                if borders[i]:
                    go_on = True
                    dr, dc = dirs[i]
                    r, c = borders[i]
                    nr, nc = r + dr, c + dc

                    if -1 < nr < 8 and -1 < nc < 8:
                        if nr in queen_dic and nc in queen_dic[nr]:
                            res.append([nr, nc])
                            borders[i] = None
                        else:
                            borders[i] = [nr, nc]
                    else:
                        borders[i] = None
                        
        return res


sol = Solution()
# p = [[[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0]]
p = [[[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4]]
print(sol.queensAttacktheKing(*p))
