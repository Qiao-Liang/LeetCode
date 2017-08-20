class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A_num = 0
        L_num = 1
        prev = None

        for ch in s:
            if ch == 'A':
                A_num += 1

                if A_num > 1:
                    return False
            
            if ch == 'L':
                if prev == 'L':
                    L_num += 1
                else:
                    L_num = 1
                
                if L_num > 2:
                    return False
            
            prev = ch

        return True

sol = Solution()
print(sol.checkRecord('PPALLL'))
        