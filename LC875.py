from math import ceil

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def is_possible(k):
            return sum((ceil(p / k)) for p in piles) <= H

        lo, hi = 1, ceil(max(piles) / ceil(H / len(piles)))

        while lo < hi:
            mid = (lo + hi) // 2

            if is_possible(mid):
                hi = mid
            else:
                lo = mid + 1
        
        return lo


sol = Solution()
piles = [3,6,7,11]
H = 8
print(sol.minEatingSpeed(piles, H))
