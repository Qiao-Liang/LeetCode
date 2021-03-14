class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = []

        for i in range(2, n + 1):
            for t in range(2, i):
                if i % t == 0:
                    break
            else:
                primes.append(i)

        np = len(primes)
        nnp = n - np
        prime_perm = 1
        non_prime_perm = 1
        
        while np > 1:
            prime_perm *= np
            np -= 1

        while nnp > 1:
            non_prime_perm *= nnp
            nnp -= 1

        return prime_perm * non_prime_perm % (10 ** 9 + 7)


sol = Solution()
# n = 5
n = 100
print(sol.numPrimeArrangements(n))
