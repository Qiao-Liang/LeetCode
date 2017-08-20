class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([s[::-1] for s in s.split(' ')])

sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))