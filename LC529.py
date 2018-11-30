class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        height = len(board)
        width = len(board[0])
        queue = [tuple(click)]
        visited = [[False] * width for _ in xrange(height)]

        def get_neighbors(row, col):
            for row_offset in xrange(-1, 2):
                for col_offset in xrange(-1, 2):
                    if (row_offset or col_offset) and -1 < row + row_offset < height and -1 < col + col_offset < width:
                        yield row + row_offset, col + col_offset

        while len(queue) > 0:
            row, col = queue.pop(0)

            if board[row][col] == 'M':
                board[row][col] = 'X'
            else:
                mine_count = sum(board[row][col] in 'MX' for row, col in get_neighbors(row, col))

                if mine_count:
                    board[row][col] = str(mine_count)
                else:
                    board[row][col] = 'B'

                    for row, col in get_neighbors(row, col):
                        if board[row][col] in 'ME' and not visited[row][col]:
                            queue.append(tuple([row, col]))
                            visited[row][col] = True

        return board


        # if board[click[0]][click[1]] == 'M':
        #     board[click[0]][click[1]] = 'X'

        #     return board

        # height = len(board)
        # width = len(board[0])
        # visited = [[False] * width for _ in xrange(height)]
        # queue = [click]

        # while len(queue) > 0:
        #     temp_queue = []
            
        #     for cell in queue:
        #         row = cell[0]
        #         col = cell[1]
        #         visited[row][col] = True
        #         count = 0
        #         temp_cells = []

        #         if row - 1 > -1:
        #             if not visited[row - 1][col] and board[row - 1][col] == 'E':
        #                 temp_cells.append([row - 1, col])

        #             if board[row - 1][col] == 'M':
        #                 count += 1

        #             if col - 1 > -1 and board[row - 1][col - 1] == 'M':
        #                 count += 1

        #             if col + 1 < width and board[row - 1][col + 1] == 'M':
        #                 count += 1

        #         if row + 1 < height:
        #             if not visited[row + 1][col] and board[row + 1][col] == 'E':
        #                 temp_cells.append([row + 1, col])

        #             if board[row + 1][col] == 'M':
        #                 count += 1

        #             if col - 1 > -1 and board[row + 1][col - 1] == 'M':
        #                 count += 1

        #             if col + 1 < width and board[row + 1][col + 1] == 'M':
        #                 count += 1

        #         if col - 1 > -1:
        #             if not visited[row][col - 1] and board[row][col - 1] == 'E':
        #                 temp_cells.append([row, col - 1])

        #             if board[row][col - 1] == 'M':
        #                 count += 1

        #         if col + 1 < width:
        #             if not visited[row][col + 1] and board[row][col + 1] == 'E':
        #                 temp_cells.append([row, col + 1])

        #             if board[row][col + 1] == 'M':
        #                 count += 1

        #         if count > 0:
        #             board[row][col] = str(count)
        #         else:
        #             board[row][col] = 'B'
                
        #         temp_queue.extend(temp_cells)

        #     queue = temp_queue

        # return board


sol = Solution()
# board = [
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]

board = [
    ["E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","M"],
    ["E","E","M","E","E","E","E","E"],
    ["M","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E"],
    ["E","E","E","E","E","E","E","E"],
    ["E","E","M","M","E","E","E","E"]]

res = sol.updateBoard(board, [0, 0])

for row in res:
    print row

[
    ["B","B","B","B","B","B","1","E"],
    ["B","1","1","1","B","B","1","M"],
    ["1","2","M","1","B","B","1","1"],
    ["M","2","1","1","B","B","B","B"],
    ["1","1","B","B","B","B","B","B"],
    ["B","B","B","B","B","B","B","B"],
    ["B","1","2","2","1","B","B","B"],
    ["B","1","M","M","1","B","B","B"]]
