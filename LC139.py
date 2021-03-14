class Solution(object):
    def wordBreak(self, s: str, wordDict) -> bool:
        len_s = len(s)
        dp = [False] * len_s
        dp[0] = True
        ws = set(wordDict)
        
        for l in range(len_s):
            for r in range(l, len_s):
                if s[l: r + 1] in ws and dp[l - 1]:
                    dp[r] = True
                    
        return dp[-1]

    def wordBreak2(self, s, wordDict):
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
