"""
Word Break
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.words = wordDict
        return self.find(s, [], "")
        
    def find(self, s, wrong_words, result):
        if len(s) == 0:
            print("Below is the result:")
            print(result)
            return True
        elif s in wrong_words:
            return False
        else:
            i = 0
            temp = ''
            
            while i < len(s):
                temp += s[i]
                
                if temp in self.words:
                    if self.find(s[i + 1:], wrong_words, result + temp + " "):
                        return True
                    else:
                        i += 1
                else:
                    i += 1
        
        wrong_words.append(temp)
        return False
