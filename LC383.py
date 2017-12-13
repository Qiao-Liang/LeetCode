class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True

        len_ran = len(ransomNote)

        if not magazine or len_ran > len(magazine):
            return False

        temp_ransom = sorted(list(ransomNote))
        temp_mag = sorted(list(magazine))

        ch = temp_ransom.pop(0)
        for m in temp_mag:
            if ch == m:
                if temp_ransom:
                    ch = temp_ransom.pop(0)
                else:
                    return True

        return False


sol = Solution()
a = "bg"
b = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(sol.canConstruct(a, b))
