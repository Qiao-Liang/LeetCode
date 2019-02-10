class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(list(J))
        res = 0

        for c in S:
            if c in jewels:
                res += 1

        return res


sol = Solution()
J = ""
S = ""
print(sol.numJewelsInStones(J, S))
        