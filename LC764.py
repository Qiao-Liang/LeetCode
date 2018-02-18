class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        if len(mines) == N ** 2:
            return 0

        matrix = [[1] * N for n in range(N)]

        def get_order(row, col):
            offset = 1

            while row - offset >= 0 and col - offset >= 0 and row + offset < N and col + offset < N \
                and matrix[row][col + offset] == 1 and matrix[row][col - offset] == 1 \
                and matrix[row + offset][col] == 1 and matrix[row - offset][col] == 1:
                offset += 1

            return offset

        for mine in mines:
            matrix[mine[0]][mine[1]] = 0

        if N & 1 == 0:
            row = col = N / 2 - 1
            dist = 1
        else:
            row = col = N / 2
            temp_ord = get_order(row, col)

            if temp_ord == row + 1:
                return temp_ord

            row -= 1
            col -= 1
            dist = 2

        max_ord = 0
        while row >= 0 and col >= 0:
            temp_max_ord = row + 1
            temp_ord = 0

            for offset in range(dist):
                if matrix[row][col + offset] == 1:
                    temp_ord = max(temp_ord, get_order(row, col + offset))

                    if temp_ord == temp_max_ord:
                        return temp_ord

                if matrix[row + offset][col + dist] == 1:
                    temp_ord = max(temp_ord, get_order(row + offset, col + dist))

                    if temp_ord == temp_max_ord:
                        return temp_ord

                if matrix[row + dist][col + dist - offset] == 1:
                    temp_ord = max(temp_ord, get_order(row + dist, col + dist - offset))

                    if temp_ord == temp_max_ord:
                        return temp_ord

                if matrix[row + dist - offset][col] == 1:
                    temp_ord = max(temp_ord, get_order(row + dist - offset, col))

                    if temp_ord == temp_max_ord:
                        return temp_ord

            max_ord = max(max_ord, temp_ord)

            if max_ord >= temp_max_ord - 1:
                return max_ord

            row -= 1
            col -= 1
            dist += 2

        return max_ord


sol = Solution()
# N = 6
# mines = [[2, 2], [2, 3], [3, 2], [3, 3]]
# N = 1
# mines = [[0, 0]]
# N = 2
# mines = [[0,0],[0,1],[1,0],[1,1]]
# N = 2
# mines = [[0,0],[0,1],[1,0]]
# N = 3
# mines = [[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
# N = 3
# mines = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
# N = 3
# mines = [[0, 0]]
N = 3
mines = [[0,0],[0,2],[1,0],[1,1],[1,2],[2,2]]
# N = 5
# mines = [[4, 2]]
# N = 5
# mines = [[1,0],[1,4],[2,4],[3,2],[4,0],[4,3]]
print(sol.orderOfLargestPlusSign(N, mines))
        