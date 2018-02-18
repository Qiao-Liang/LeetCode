class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n

        layers = 1

        while True:
            temp = (1 + layers) * layers / 2
            if temp < n:
                layers *= 2
            elif temp > n:
                break
            else:
                return layers

        upper = layers
        lower = upper / 2

        while upper - lower > 1:
            mid = (upper + lower) / 2
            temp = (1 + mid) * mid / 2

            if temp < n:
                lower = mid
            elif temp > n:
                upper = mid
            else:
                return mid

        return lower


sol = Solution()
print(sol.arrangeCoins(3))
