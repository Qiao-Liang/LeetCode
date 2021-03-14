class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        visited = set([(0, 0)])
        queue = [(0, 0)]
        res = 0
        
        while queue:
            temp = []
            
            for tx, ty in queue:
                if tx == x and ty == y:
                    return res

                fx = x - tx
                fy = y - ty

                if fx >= 0 and fy >= 0:
                    d = [(1, 2), (2, 1)]
                elif fx >= 0 and fy <= 0:
                    d = [(1, -2), (2, -1)]
                elif fx <= 0 and fy >= 0:
                    d = [(-1, 2), (-2, 1)]
                elif fx <= 0 and fy <= 0:
                    d = [(-1, -2), (-2, -1)]
                
                for dx, dy in d:
                    dx += tx
                    dy += ty
                    
                    if (dx, dy) not in visited:
                        visited.add((dx, dy))
                        temp.append((dx, dy))
                        
            res += 1
            queue = temp


sol = Solution()
# p = [2, 1]
# p = [5, 5]
# p = [-84, 170]
p = [136, -63]
print(sol.minKnightMoves(*p))
