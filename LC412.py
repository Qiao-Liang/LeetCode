class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [None] * n

        for idx in xrange(1, n + 1):
            if idx % 15 == 0:
                res[idx - 1] = "FizzBuzz"
            elif idx % 3 == 0:
                res[idx - 1] = "Fizz"
            elif idx % 5 == 0:
                res[idx - 1] = "Buzz"
            else:
                res[idx - 1] = str(idx)
        
        return res


sol = Solution()
print sol.fizzBuzz(15)
