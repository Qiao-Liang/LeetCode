class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        matrix = [[0] * len_s for _ in range(len_s)]

        for idx in range(len_s):
            matrix[idx][idx] = 1

        for idx in range(1, len_s):
            if s[idx - 1] == s[idx]:
                matrix[idx - 1][idx] = 1

        for length in range(3, len_s + 1):
            left = 0
            right = length - 1

            while right < len_s:
                if matrix[left + 1][right - 1] == 1 and s[left] == s[right]:
                    matrix[left][right] = 1

                left += 1
                right += 1
        
        return sum(map(sum, matrix))


sol = Solution()
s = "abcba"
# s = "aaa"
# s = "abc"
# s = "aba"
# s = "aaaaa"
print(sol.countSubstrings(s))
        