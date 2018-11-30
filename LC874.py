class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        def move_up((x, y), dist):
            min_dist = dist

            for obs in obstacles:
                if obs[0] == x and obs[1] > y and obs[1] - y - 1 < min_dist:
                    min_dist = obs[1] - y - 1

            return (x, y + min_dist)
        
        def move_right((x, y), dist):
            min_dist = dist

            for obs in obstacles:
                if obs[1] == y and obs[0] > x and obs[0] - x - 1 < min_dist:
                    min_dist = obs[0] - x - 1

            return (x + min_dist, y)

        def move_down((x, y), dist):
            min_dist = dist

            for obs in obstacles:
                if obs[0] == x and obs[1] < y and y - obs[1] - 1 < min_dist:
                    min_dist = y - obs[1] - 1

            return (x, y - min_dist)

        def move_left((x, y), dist):
            min_dist = dist

            for obs in obstacles:
                if obs[1] == y and obs[0] < x and x - obs[0] - 1 < min_dist:
                    min_dist = x - obs[0] - 1
            
            return (x - min_dist, y)
        
        directions = [move_up, move_right, move_down, move_left]
        direction = 0
        curr_pos = (0, 0)

        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction + 3) % 4
            else:
                curr_pos = directions[direction](curr_pos, command)

        return curr_pos[0] ** 2 + curr_pos[1] ** 2


sol = Solution()
commands = [4,-1,4,-2,4]
obstacles = [[2, 4]]
print sol.robotSim(commands, obstacles)
        