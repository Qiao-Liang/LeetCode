class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return False

        self.res = True

        def recurse(n, is_a):
            divs = [d for d in range(1, n) if n % d == 0]

            if n == 1 and is_a:
                self.res = False
            else:
                for div in divs:
                    recurse(n - div, not is_a)
        
        recurse(N, True)
        return self.res


sol = Solution()
n = 4
print(sol.divisorGame(n))
