class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        i1 = i2 = i3 = 0
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False
        
        while i3 < len3:
            if i1 < len1 and i2 < len2:
                if s1[i1] == s2[i2] == s3[i3]:
                    t1 = i1
                    t2 = i2

                    while t1 < len1 and t2 < len2 and i3 < len3 and s1[t1] == s2[t2] == s3[i3]:
                        t1 += 1
                        t2 += 1
                        i3 += 1

                    if t1 < len1 and i3 < len3 and s1[t1] == s3[i3]:
                        i1 = t1

                        while i1 < len1 and i3 < len3 and s1[i1] == s3[i3]:
                            i1 += 1
                            i3 += 1
                    elif t2 < len2 and i3 < len3 and s2[t2] == s3[i3]:
                        i2 = t2

                        while i2 < len2 and i3 < len3 and s2[i2] == s3[i3]:
                            i2 += 1
                            i3 += 1
                    else:
                        return False
                elif s1[i1] == s3[i3]:
                    i1 += 1
                    i3 += 1
                elif s2[i2] == s3[i3]:
                    i2 += 1
                    i3 += 1
                else:
                    return False
            elif i1 < len1:
                if s1[i1] == s3[i3]:
                    i1 += 1
                    i3 += 1
                else:
                    return False
            elif i2 < len2:
                if s2[i2] == s3[i3]:
                    i2 += 1
                    i3 += 1
                else:
                    return False
            else:
                return False
        
        return True


sol = Solution()
# params = ["aabcc","dbbca","aadbbcbcac"]
# params = ["aabcc","dbbca","aadbcbbcac"]
params = ["aa","ab","aaba"]
print(sol.isInterleave(*params))
