class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return len([w for w in s.split(' ') if w != ''])

        last_ch = ' '
        count = 0
        for c in s:
            if c != ' ' and last_ch == ' ':
                count += 1
            
            last_ch = c

        return count


sol = Solution()
print(sol.countSegments(" Hello, my name is John "))
