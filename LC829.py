class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        while N & 1 == 0:
            N >>= 1
            
        res = 1
        k = 3
        
        while k ** 2 <= N:
            count = 0
            
            while N % k == 0:
                N /= k
                count += 1
                
            res *= count + 1
            k += 2
            
        if N > 1:
            res *= 2
            
        return res


        # if N == 1:
        #     return 1

        # res = 0
        # odd = 1
        # bound = N // 2
        
        # while odd <= bound:
        #     if N % odd == 0:
        #         res += 1
        #         print(odd)
                
        #     odd += 2
            
        # if N & 1 and N % 2 == 1:
        #     res += 1
        
        # return res


sol = Solution()
n = 2619722
# n = 9
print(sol.consecutiveNumbersSum(n))
