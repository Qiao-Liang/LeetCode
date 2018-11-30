class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        len_s = len(s)
        s = list(s)
        slow = fast = 0

        while slow < len_s:
            if s[slow] != ' ':
                fast = slow

                while fast < len_s and s[fast] != ' ':
                    fast += 1

                left = slow
                right = fast - 1

                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1

                slow = fast
            else:
                slow += 1
        
        return ''.join(s)


        # return ' '.join([s[::-1] for s in s.split(' ')])

sol = Solution()
print(sol.reverseWords("Let's take LeetCode contest"))