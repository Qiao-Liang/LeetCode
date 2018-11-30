class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        len_bed = len(flowerbed)
        bound = len_bed - 1

        for idx in xrange(0, len_bed):
            if flowerbed[idx] == 0 and (idx == 0 or flowerbed[idx - 1] == 0) and (idx == bound or flowerbed[idx + 1] == 0):
                count += 1
                flowerbed[idx] = 1

        return count >= n


sol = Solution()
flowerbed = [0, 0, 1, 0, 1]
n = 1
print sol.canPlaceFlowers(flowerbed, n)
        