class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)
        res = ''
        
        if len1 < len2:
            str1, str2 = str2, str1
            len1, len2 = len2, len1
        
        for bound in range(1, len2 + 1):
            temp = str2[:bound]
            
            if len1 % bound == 0 and len2 % bound == 0 and temp * int(len1 / bound) == str1:
                res = temp
        
        return res


sol = Solution()
s1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
s2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print(sol.gcdOfStrings(s1, s2))
