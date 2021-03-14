class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        res1 = res2 = 0
        temp = start
        len_dist = len(distance)
        
        while temp != destination:
            res1 += distance[temp]
            temp += 1
            temp %= len_dist
            
        temp = destination
        
        while temp != start:
            res2 += distance[temp]
            temp += 1
            temp %= len_dist
            
        return min(res1, res2)


sol = Solution()
p = [[1,2,3,4,], 0, 3]
print(sol.distanceBetweenBusStops(*p))
