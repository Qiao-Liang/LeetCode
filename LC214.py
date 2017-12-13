class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        len_s = len(s)

        for idx in range(len_s - 1, 0, -1):
            left = 0
            right = idx
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    break
            
            if right < left:
                if idx == len_s - 1:
                    return s
                else:
                    return s[idx + 1:][::-1][:] + s
        
        return s[1:][::-1] + s

sol = Solution()
print(sol.shortestPalindrome("aba"))
