class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        root = 1

        while True:
            temp = root ** 2

            if temp < x:
                root <<= 1
            elif temp > x:
                break
            else:
                return root

        left = right = root
        left >>= 1

        while left <= right:
            mid = (left + right) // 2

            if mid ** 2 <= x:
                if x < (mid + 1) ** 2:
                    return mid
                else:
                    left = mid + 1
            else:
                right = mid - 1


        # if x == 0:
        #     return 0

        # low = 1
        # high = 2

        # while True:
        #     low_sqr = low ** 2
        #     high_sqr = high ** 2

        #     if low_sqr == x:
        #         return low
        #     elif high_sqr == x:
        #         return high
        #     elif low ** 2 <= x <= high ** 2:
        #         break
        #     else:
        #         low <<= 1
        #         high <<= 1

        # while low <= high:
        #     mid = (low + high) / 2
        #     mid_sqr = mid ** 2
        #     mid_plus_sqr = (mid + 1) ** 2
        #     mid_min_sqr = (mid - 1) ** 2

        #     if mid_sqr <= x < mid_plus_sqr:
        #         return mid

        #     if mid_min_sqr <= x < mid_sqr:
        #         return mid - 1

        #     if mid_plus_sqr < x:
        #         low = mid + 1

        #     if x < mid_min_sqr:
        #         high = mid - 1


sol = Solution()
# print(sol.mySqrt(1825989974))
print(sol.mySqrt(4))
