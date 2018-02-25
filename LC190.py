class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        temp = 1
        bit = 0
        res = 0

        while temp <= n:
            temp <<= 1
            bit += 1

        temp >>= 1
        bit -= 1
        base = 1 << (31 - bit)

        while bit >= 0:
            if n >= temp:
                res += base
                n -= temp
            
            temp >>= 1
            base <<= 1
            bit -= 1

        return res


sol = Solution()
print sol.reverseBits(1)
