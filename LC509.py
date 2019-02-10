class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        else:
            a = 0
            b = 1
            
            while N > 1:
                a, b = b, a + b
                N -= 1
                
            return b
        
        self.dic = {0: 0, 1: 1}
        
        def recurse(n):
            if n in self.dic:
                return self.dic[n]

            self.dic[n] = recurse(n - 1) + recurse(n - 2)
            return self.dic[n]
        
        return recurse(N)
