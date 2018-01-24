class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_num = [1] * n
        idx_2, idx_3, idx_5 = 0, 0, 0

        while n > 1:
            prod_2, prod_3, prod_5 = ugly_num[idx_2] * 2, ugly_num[idx_3] * 3, ugly_num[idx_5] * 5
            min_prod = min(prod_2, prod_3, prod_5)

            if min_prod == prod_2:
                idx_2 += 1
            if min_prod == prod_3:
                idx_3 += 1
            if min_prod == prod_5:
                idx_5 += 1

            n -= 1
            ugly_num[-n] = min_prod

        return ugly_num[-1]


sol = Solution()
print(sol.nthUglyNumber(10))
