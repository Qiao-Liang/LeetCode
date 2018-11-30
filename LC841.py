class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        stack = [0]

        while stack:
            if rooms[stack[-1]]:
                stack.append(rooms[stack[-1]].pop())
            else:
                visited[stack[-1]] = True
                stack.pop()

        return len([visited_room for visited_room in visited if visited_room]) == len(rooms)


sol = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
# rooms = [[1],[2],[3],[]]
print(sol.canVisitAllRooms(rooms))            
