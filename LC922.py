class Solution:
    def sortArrayByParityII(self, a):
        io = 1
        
        for ie in range(0, len(a), 2):
            if a[ie] & 1 == 1:
                while a[io] & 1 == 1:
                    io += 2
                    
                a[ie], a[io] = a[io], a[ie]
                
        return a


sol = Solution()
a = [888,505,627,846]
print(sol.sortArrayByParityII(a))
