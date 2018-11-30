class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_seq = [ord(x) - ord('a') for x in s1]
        s2_seq = [ord(x) - ord('a') for x in s2]
        len1 = len(s1)

        s1_stat = [0] * 26
        for num in s1_seq:
            s1_stat[num] += 1
        
        win = [0] * 26
        for idx, val in enumerate(s2_seq):
            win[val] += 1
            if idx >= len1:
                win[s2_seq[idx - len1]] -= 1
            
            if win == s1_stat:
                return True

        return False
