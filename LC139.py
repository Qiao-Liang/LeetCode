"""
Word Break
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                print("*" * 30)
                print("i: ", i)
                print("j: ", j)
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    print(s[i: j + 1])
                    print(dp)
                print("*" * 30)
                    
        return dp[-1]