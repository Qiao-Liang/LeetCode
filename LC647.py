class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        matrix = [[0] * len_s for _ in xrange(len_s)]

        for idx in xrange(len_s):
            matrix[idx][idx] = 1

        for idx in xrange(1, len_s):
            if s[idx - 1] == s[idx]:
                matrix[idx - 1][idx] = 1

        for length in xrange(2, len_s + 1):
            left = 0
            right = length - 1

            while right < len_s:
                if matrix[left + 1][right - 1] == 1 and s[left] == s[right]:
                    matrix[left][right] = 1

                left += 1
                right += 1
        
        return sum(map(sum, matrix))


sol = Solution()
# s = "abcba"
# s = "aaa"
# s = "abc"
s = "aaaaa"
print sol.countSubstrings(s)
        