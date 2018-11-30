class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        len_g = len(g)
        len_s = len(s)
        count = 0
        idx_g = idx_s = 0

        while idx_g < len_g and idx_s < len_s:
            if s[idx_s] < g[idx_g]:
                idx_s += 1
            else:
                count += 1
                idx_g += 1
                idx_s += 1

        return count


sol = Solution()
g, s = [1, 2], [1, 2, 3]
print sol.findContentChildren(g, s)
