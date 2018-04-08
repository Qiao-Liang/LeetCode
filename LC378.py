class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rank = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low < high:
            mid = (high + low) >> 1
            cnt = 0
            row = 0
            col = rank - 1

            while row < rank and col > -1:
                if matrix[row][col] > mid:
                    col -= 1
                else:
                    cnt += col + 1
                    row += 1

            if cnt < k:
                low = mid + 1
            else:
                high = mid

        return low

    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return None

        len_matrix = len(matrix)

        if len_matrix == 0:
            return None

        idx_list = [0] * len_matrix
        row_limit = len(matrix[0])

        while k > 0:
            temp_min = float('inf')
            temp_idx = 0

            for idx, row in enumerate(matrix):
                if idx_list[idx] < row_limit and row[idx_list[idx]] < temp_min:
                    temp_min = row[idx_list[idx]]
                    temp_idx = idx
                    
            idx_list[temp_idx] += 1
            k -= 1

        return temp_min

    def kthSmallest3(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return None

        len_matrix = len(matrix)
        
        if len_matrix == 0:
            return None

        srt = 0
        len_row = len(matrix[0])
        end = len_matrix * len_row
        target = k - 1
        target_row = target / len_row
        target_col = target % len_row

        while True:
            srt_row = srt / len_row
            srt_col = srt % len_row
            pivot = matrix[target_row][target_col]
            wall = srt
            matrix[target_row][target_col], matrix[srt_row][srt_col] = matrix[srt_row][srt_col], matrix[target_row][target_col]

            for idx in xrange(srt + 1, end):
                idx_row = idx / len_row
                idx_col = idx % len_row

                if matrix[idx_row][idx_col] < pivot:
                    wall += 1

                    if idx > wall:
                        wall_row = wall / len_row
                        wall_col = wall % len_row

                        matrix[idx_row][idx_col], matrix[wall_row][wall_col] = matrix[wall_row][wall_col], matrix[idx_row][idx_col]

            wall_row = wall / len_row
            wall_col = wall % len_row
            matrix[srt_row][srt_col], matrix[wall_row][wall_col] = matrix[wall_row][wall_col], matrix[srt_row][srt_col]

            if wall < target:
                srt = wall + 1
            elif wall > target:
                end = wall
            else:
                return matrix[wall_row][wall_col]

    def kthSmallest4(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low = matrix[0][0]
        high = matrix[-1][-1]
        
        while low < high:
            mid = (high + low) >> 1
            cnt = last = 0

            for row in matrix:
                for col in row:
                    if col > mid:
                        break
                    else:
                        cnt += 1
                        last = max(col, last)

            if cnt < k:
                low = mid + 1
            elif cnt > k:
                high = mid
            else:
                return last

        return low


sol = Solution()
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ]
matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]]
# matrix = [[-5]]
# k = 5

for k in xrange(1, 26):
    print sol.kthSmallest(matrix, k)

# print sol.kthSmallest(matrix, 1)
