class Solution:
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        x, y = 1, 2
        res = 1

        while num:
            if num & 3 == 3:
                res = 0
            
            res += x * (num & 1)
            num >>= 1
            x, y = y, x + y
        
        return res

        # self.res = 1
        # self.visited = set([])

        # def dfs(n):            
        #     if n <= num and n & 3 != 3:
        #         self.res += 1
        #         n <<= 1
        #         dfs(n)
        #         dfs(n + 1)
        
        # dfs(1)

        # return self.res
        
        # res = 0

        # while num > 0:
        #     temp = 3
        #     res += 1

        #     while temp <= num:
        #         if temp & num == temp:
        #             res -= 1
        #             break
                
        #         temp <<= 1

        #     num -= 1

        # return res + 1


sol = Solution()
num = 84
print(sol.findIntegers(num))
