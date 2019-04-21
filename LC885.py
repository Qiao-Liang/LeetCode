class Solution(object):
    def spiralMatrixIII(self, r, c, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        count = 0
        res = [[r0, c0]]
        step = 1
        total = R * C - 1

        while count < total:
            temp_c = c0 + step + 1

            while True:
                if c0 + 1 < temp_c:
                    c0 += 1

                    if -1 < r0 < R and -1 < c0 < C:
                        count += 1
                        res.append([r0, c0])
                else:
                    break

            temp_r = r0 + step + 1

            while True:
                if r0 + 1 < temp_r:
                    r0 += 1

                    if -1 < r0 < R and -1 < c0 < C:
                        count += 1
                        res.append([r0, c0])
                else:
                    break

            step += 1
            temp_c = c0 - step - 1

            while True:
                if c0 - 1 > temp_c:
                    c0 -= 1

                    if -1 < r0 < R and -1 < c0 < C:
                        count += 1
                        res.append([r0, c0])
                else:
                    break

            temp_r = r0 - step - 1

            while True:
                if r0 - 1 > temp_r:
                    r0 -= 1

                    if -1 < r0 < R and -1 < c0 < C:
                        count += 1
                        res.append([r0, c0])
                else:
                    break

            step += 1

        return res


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
