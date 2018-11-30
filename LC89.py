class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        n -= 1
        add_on = 2
        res = [0, 1]

        while n > 0:
            res.extend([val + add_on for val in reversed(res)])
            
            n -= 1
            add_on <<= 1

        return res


sol = Solution()
print sol.grayCode(2)
        