class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        bin_n = bin(N).split('b')[1]
        len_n = len(bin_n)
        max_gap = 0
        curr = last = 0

        while curr < len_n:
            if bin_n[curr] == '1':
                max_gap = max(max_gap, curr - last)
                last = curr
                
            curr += 1

        return max_gap


sol = Solution()
print sol.binaryGap(8)
        