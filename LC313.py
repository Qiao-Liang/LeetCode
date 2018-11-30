from heapq import heapify, heappush, heappop

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1] * n
        curr = 1
        indices = [0] * len(primes)
        heap = [(val, idx) for idx, val in enumerate(primes)]
        
        heapify(heap)
        
        while curr < n:
            temp, idx = heappop(heap)

            if temp != res[curr - 1]:
                res[curr] = temp
                curr += 1

            indices[idx] += 1
            heappush(heap, (primes[idx] * res[indices[idx]], idx))

        return res[-1]


sol = Solution()
primes = [2, 7, 13, 19]
print sol.nthSuperUglyNumber(12, primes)
