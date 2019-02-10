class Solution(object):
    def spiralMatrixIII(self, r, c, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        visits = []
        x, y = r0, c0
        step = 0
        count = r * c

        while len(visits) < count:

            step += 1
            for j in range(y, y + step): # right: step
                if 0 <= j < c and 0 <= x < r:
                    visits.append([x, j])
            y += step

            for i in range(x, x + step): # down: step
                if 0 <= i < r and 0 <= y < c:
                    visits.append(([i, y]))
            x += step

            step += 1 # increase the step
            for j in range(y, y - step, -1): # left: step + 1
                if 0 <= j < c and 0 <= x < r:
                    visits.append([x, j])
            y -= step

            for i in range(x, x - step, -1): # up: step + 1
                if 0 <= i < r and 0 <= y < c:
                    visits.append(([i, y]))
            x -= step

        return visits

        # row_low = 0
        # row_high = R - 1
        # col_low = 0
        # col_high = C - 1
        # count = R * C
        # res = [None] * count
        # idx = 0

        # def add_point(r, c):
        #     nonlocal idx, row_low, row_high, col_low, col_high, count

        #     if count > 0 and row_low <= r <= row_high and col_low <= c <= col_high:
        #         res[idx] = [r, c]
        #         count -= 1
        #         idx += 1

        # add_point(r0, c0)
        # c0 += 1
        # add_point(r0, c0)
        # r0 += 1
        # add_point(r0, c0)
        # c0 -= 1
        # add_point(r0, c0)
        # length = 3
        # c0 -= 1

        # while count > 0:
        #     temp_count = length
            
        #     while temp_count > 0:
        #         add_point(r0, c0)
        #         r0 -= 1
        #         temp_count -= 1

        #     r0 += 1
        #     c0 += 1
        #     temp_count = length

        #     while temp_count > 0:
        #         add_point(r0, c0)
        #         c0 += 1
        #         temp_count -= 1

        #     r0 += 1
        #     c0 -= 1
        #     temp_count = length
            
        #     while temp_count > 0:
        #         add_point(r0, c0)
        #         r0 += 1
        #         temp_count -= 1

        #     c0 -= 1
        #     r0 -= 1
        #     temp_count = length

        #     while temp_count > 0:
        #         add_point(r0, c0)
        #         c0 -= 1
        #         temp_count -= 1

        #     length += 2
        
        # return res


sol = Solution()
R = 5
C = 6
r0 = 1
c0 = 4
print(sol.spiralMatrixIII(R, C, r0, c0))
