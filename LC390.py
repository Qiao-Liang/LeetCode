class Solution:
    def lastRemaining(self, n: int) -> int:
        if n < 3:
            return n
        else:
            l, r = 2, n - 1 if n & 1 else n
            ln = n // 2
            d = 2
            right = True
            
            while l < r:
                if right:
                    r -= d

                    if ln & 1:
                        l += d
                else:
                    l += d

                    if ln & 1:
                        r -= d

                ln //= 2
                d <<= 1
                right = not right
            
            return l


sol = Solution()
print(sol.lastRemaining(10))
