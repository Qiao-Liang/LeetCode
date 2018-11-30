class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True

        if num < 0:
            return False

        lower = 1
        upper = num

        while lower <= upper:
            mid = (lower + upper) // 2
            temp = mid ** 2

            if temp < num:
                lower = mid + 1
            elif temp > num:
                upper = mid - 1
            else:
                return True

        return False


        # if num == 0:
        #     return True

        # if num < 0:
        #     return False

        # upper_bound = 1

        # while True:
        #     temp = upper_bound ** 2

        #     if temp < num:
        #         upper_bound <<= 1
        #     elif temp > num:
        #         break
        #     else:
        #         return True

        # lower_bound = upper_bound >> 1

        # while lower_bound <= upper_bound:
        #     mid = (lower_bound + upper_bound) // 2
        #     temp = mid ** 2

        #     if temp > num:
        #         upper_bound = mid - 1
        #     elif temp < num:
        #         lower_bound = mid + 1
        #     else:
        #         return True

        # return False


        # i = 0
        # while i * i < num:
        #     i += 1
        
        # return i * i == num


sol = Solution()
print(sol.isPerfectSquare(81))
