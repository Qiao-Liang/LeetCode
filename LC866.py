class Solution:
    def primePalindrome(self, N: int) -> int:
        p = 2
        bound = min(N * 100, 10 ** 8)
        prime = [True] * (bound + 1)

        while p <= bound:
            t = p ** 2

            if prime[p]:
                if p >= N and str(p) == str(p)[::-1]:
                    return p

                for i in range(t, bound + 1, p):
                    prime[i] = False
            
            p += 1


sol = Solution()
n = 13
print(sol.primePalindrome(n))
