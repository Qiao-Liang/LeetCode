class Solution:
    def shortestDistanceColor(self, colors, queries):
        len_c = len(colors)
        res = [-1] * len(queries)
        memo = {}
        
        for i, (qi, qc) in enumerate(queries):
            if (qi, qc) in memo:
                res[i] = memo[(qi, qc)]
            else:
                l = r = qi
                d = 0
                
                while l > -1 or r < len_c:
                    if (l > -1 and colors[l] == qc) or (r < len_c and colors[r] == qc):
                        res[i] = d
                        memo[(qi, qc)] = d
                        break
                    
                    l -= 1
                    r += 1
                    d += 1
                
        return res


sol = Solution()
# colors = [1,1,2,1,3,2,2,3,3]
# queries = [[1,3],[2,2],[6,1]]
colors = [1,2]
queries = [[0,3]]
print(sol.shortestDistanceColor(colors, queries))
