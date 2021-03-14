class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            t = [0, 1, 1]
            i = -1
            
            while n > 2:
                i += 1
                t[i % 3] = sum(t)
                n -= 1
            
            return t[i % 3]


sol = Solution()
print(sol.tribonacci(25))
