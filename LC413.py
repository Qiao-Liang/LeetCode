class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        len_A = len(A)
        two_arith = [0] * (len_A - 1)
        count = 1
        two_counts = []
        res = 0

        for idx in xrange(0, len_A - 1):
            two_arith[idx] = A[idx + 1] - A[idx]

        for idx in xrange(0, len(two_arith) - 1):
            if two_arith[idx] == two_arith[idx + 1]:
                count += 1
            else:
                two_counts.append(count)
                count = 1

        two_counts.append(count)
        
        for count in two_counts:
            temp = count - 1
            while temp > 0:
                res += temp
                temp -= 1

        return res


sol = Solution()
a = [1, 2, 3, 4]
print sol.numberOfArithmeticSlices(a)
