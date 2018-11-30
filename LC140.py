class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.res = []
        self.temp_words = []
        self.string = s
        self.bound = len(s)
        self.dict = wordDict

        def dfs(start_idx):
            for temp_bound in xrange(start_idx + 1, self.bound + 1):
                if self.string[start_idx: temp_bound] in self.dict:
                    self.temp_words.append(self.string[start_idx: temp_bound])

                    if temp_bound == self.bound:
                        self.res.append(' '.join(self.temp_words))
                    else:
                        dfs(temp_bound)

                    self.temp_words.pop()

        dfs(0)

        return self.res

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res


sol = Solution()
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
print sol.wordBreak(s, wordDict)
print sol.wordBreak2(s, wordDict)
