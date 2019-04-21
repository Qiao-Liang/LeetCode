class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        temp = [int(n) for n in str(N + 1)]
        res, len_temp = 0, len(temp)

        def get_perm(cand_num, digits):
            temp = digits
            res = 1

            while temp > 0:
                res *= cand_num
                cand_num -= 1
                temp -= 1

            return res

        for i in range(1, len_temp):
            res += 9 * get_perm(9, i - 1)
        
        seen = set()

        for idx, n in enumerate(temp):
            for m in range(0 if idx else 1, n):
                if m not in seen:
                    res += get_perm(9 - idx, len_temp - idx - 1)
            
            if n in seen:
                break
            
            seen.add(n)

        return N - res


sol = Solution()
n = 120
print(sol.numDupDigitsAtMostN(n))
