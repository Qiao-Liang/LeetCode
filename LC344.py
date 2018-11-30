class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        left = 0
        right = len(s) - 1
        list_s = list(s)

        while left < right:
            list_s[left], list_s[right] = list_s[right], list_s[left]
            left += 1
            right -= 1

        return ''.join(list_s)


sol = Solution()
s = "hello"
print(sol.reverseString(s))
