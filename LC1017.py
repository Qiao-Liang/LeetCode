class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return '0'
        
        res = ""

        while N != 0: 
            remainder = N % -2 
            N //= -2

            if remainder < 0: 
                remainder += 2
                N += 1
    
            res = str(remainder) + res 
            
        return res


sol = Solution()
n = 4
print(sol.baseNeg2(4))
