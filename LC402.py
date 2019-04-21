class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res_len = len(num) - k

        if res_len == 0:
            return '0'
        
        stack = []

        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1

            stack.append(n)

        return ''.join(stack[:res_len]).lstrip('0') or '0'


sol = Solution()
num = "1234567890"
k = 9
print(sol.removeKdigits(num, k))
