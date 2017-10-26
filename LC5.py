class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_str = ""
        max_len = 0
        s_len = len(s)

        for head in range(s_len):
            tail = head
            while tail < s_len:
                temp = s[head: tail]
                temp_len = len(temp)

                if temp == temp[::-1] and temp_len > max_len:
                    max_len = temp_len
                    max_str = temp
                
                tail += 1

        return max_str

sol = Solution()
print(sol.longestPalindrome("babad"))
