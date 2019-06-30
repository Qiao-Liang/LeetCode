class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y, dx, dy = 0, 0, 0, 1

        for ins in instructions:
            if ins == 'R':
                dx, dy = dy, -dx
            elif ins == 'L':
                dx, dy = -dy, dx
            elif ins == 'G':
                x, y = x + dx, y + dy
        
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)

        # x = 0
        # y = 0
        # dirt = 0
    
        # for move in instructions:
        #     if move == 'R':
        #         dirt = (dirt + 1) % 4
        #     elif move == 'L':
        #         dirt = (4 + dirt - 1) % 4
        #     else:
        #         if dirt == 0:
        #             y += 1
        #         elif dirt == 1:
        #             x += 1
        #         elif dirt == 2:
        #             y -= 1
        #         else: 
        #             x -= 1
    
        # return (x == 0 and y == 0)