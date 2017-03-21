"""
Valid Anagram
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        
        for ch in s:
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
        
        for ch in t:
            if ch in dict:
                dict[ch] -= 1
            else:
                return False
        
        for k, v in dict.items():
            if v != 0:
                return False
        
        return True