class Solution:
    def shiftGrid(self, grid, k: int):
        r = len(grid)
        c = len(grid[0])
        
        if k == r * c:
            return grid
        
        flat = []
        res = []
        
        for row in grid:
            flat.extend(row)
        
        len_flat = len(flat)
        k %= len_flat
        flat = flat[-k:] + flat[:-k]
        s = 0
        e = c
        
        while s < len_flat:
            res.append(flat[s: e])
            s += c
            e += c
            
        return res


sol = Solution()
# p = [[[1,2,3],[4,5,6],[7,8,9]], 1]
# p = [[[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4]
p = [[[1],[2],[3],[4],[7],[6],[5]], 23]
print(sol.shiftGrid(*p))
