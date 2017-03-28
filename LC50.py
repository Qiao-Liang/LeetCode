class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if n == 0:
        #     return 1
        # else:
        #     temp = self.myPow(x, n // 2)
            
        #     if n % 2 == 0:
        #         return temp * temp
        #     else:
        #         if n > 0:
        #             return temp * temp * x
        #         else:
        #             return temp * temp / x
        if n == 0:
            return 1
        else:
            is_minus = False
            
            if n < 0:
                is_minus = True
                n = -n

            if n == 1:
                result = x
            else:
                temp = x
                result = 1

                while n > 1:
                    m = 2
                    while m <= n:
                        temp = temp * temp
                        m = m * 2
                    
                    n = n - m / 2
                    result = result * temp
                    temp = x
            
                if n == 1:
                    result = result * x

            if is_minus:
                return 1 / result
            else:
                return result
        