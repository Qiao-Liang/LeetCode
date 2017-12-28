class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        
        primes = [1] * n
        primes[0] = primes[1] = 0

        for idx in range(2, int(pow(n, 0.5)) + 1):
            if primes[idx]:
                primes[idx * idx: n : idx] = [0] * len(primes[idx * idx: n : idx])

        return sum(primes)


sol = Solution()
print(sol.countPrimes(100))
