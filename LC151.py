class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = [word for word in s.strip().split(' ') if word != '']
        left = 0
        right = len(s_list) - 1

        while left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return ' '.join(s_list)


sol = Solution()
# s = "the sky is blue"
s = "   a   b "
print sol.reverseWords(s)
        