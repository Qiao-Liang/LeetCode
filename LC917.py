class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""

        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        left = 0
        right = len(S) - 1
        S = list(S)

        while left < right:
            if S[left] in letters and S[right] in letters:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
            
            if S[left] not in letters:
                left += 1

            if S[right] not in letters:
                right -= 1

        return ''.join(S)


sol = Solution()
print sol.reverseOnlyLetters("")
        