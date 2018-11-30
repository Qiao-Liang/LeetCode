class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper_count = lower_count = 0
        len_word = len(word)
        
        for ch in word:
            if ch in upper:
                upper_count += 1
            elif ch in lower:
                lower_count += 1

        return len_word == upper_count or len_word == lower_count or (word[0] in upper and lower_count == len_word - 1)
