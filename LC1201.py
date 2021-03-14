# from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            while x:
                t = x
                x = y % x
                y = t
            
            return y
        
        l, r = 1, max(a, b, c) * n
        ab = a * b // gcd(a, b)
        ac = a * c // gcd(a, c)
        bc = b * c // gcd(b, c)
        abc = ab * c // gcd(ab, c)

        while l < r:
            m = (l + r) // 2

            if m // a + m // b + m // c - (m // ab + m // ac + m // bc) + m // abc < n:
                l = m + 1
            else:
                r = m
        
        return r

        # while a < b:
        #     a += a
        #     n -= 1

        # res = None
        # h = [(a, a), (b, b), (c, c)]
        # keys = set([a, b, c])
        
        # while n:
        #     res, k = heappop(h)
        #     keys.remove(res)
        #     temp = res + k

        #     while temp in keys:
        #         temp += k

        #     keys.add(temp)
        #     heappush(h, (temp, k))
        #     n -= 1
        
        # return res


sol = Solution()
# p = [3, 2, 3, 5]
# p = [4, 2, 3, 4]
# p = [5, 2, 11, 13]
p = [1000000000, 2, 217983653, 336916467]
print(sol.nthUglyNumber(*p))
