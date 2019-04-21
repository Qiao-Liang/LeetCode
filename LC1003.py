class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        while len(S) > 3:
            not_found = True

            for idx in range(len(S) - 3):
                if S[idx: idx + 3] == 'abc':
                    S = S[:idx] + S[idx + 3:]
                    not_found = False
                    break

            if not_found:
                return False

        return S == 'abc'


sol = Solution()
# s = "aabcbc"
# s = "abcabcababcc"
s = "cababc"
# s = "ababccabc"
print(sol.isValid(s))
