class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"

        res = num[:len(num) - k]

        # return str(min(int(sorted(list(num[:k + 1]))[0] + num[k + 1:]), int(num[:-(k + 1)] + sorted(list(num[len(num) - k - 1:]))[0])))


sol = Solution()
print sol.removeKdigits("112", 1)
        