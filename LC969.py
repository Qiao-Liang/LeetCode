class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        res = []
        
        while n > 0:
            mi, mv = 0, A[0]
            
            for i, v in enumerate(A[:n]):
                if v > mv:
                    mv = v
                    mi = i
            
            mi += 1
            res.append(mi)
            res.append(n)
            A = (A[mi - 1::-1] + A[mi:n])[::-1] + A[n:]
            n -= 1
        
        return res


sol = Solution()
a = [3,2,4,1]
print(sol.pancakeSort2(a))
