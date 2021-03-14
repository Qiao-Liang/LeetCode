class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        temp = []
        temp_n = N
        
        while temp_n > 0:
            temp.append(temp_n % 10)
            temp_n //= 10
            
        k = len(temp)
        return N == sum(list(map(lambda n: n ** k, temp)))
        

sol = Solution()
print(sol.isArmstrong(153))
