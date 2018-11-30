class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        queue = [beginWord]
        wordSet = set(wordList)
        count = 0

        while queue:
            temp_queue = []

            for begin in queue:
                for idx in xrange(len(begin)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        temp = list(begin)
                        temp[idx] = ch
                        temp = ''.join(temp)

                        if temp in wordSet:
                            if temp == endWord:
                                return count + 2

                            temp_queue.append(temp)
                            wordSet.remove(temp)
            
            queue = temp_queue
            count += 1

        return 0

        # self.res = len(wordList)

        # def recurse(begin, end, idx, wordList, count):
        #     if begin == end:
        #         self.res = min(self.res, count) + 1

        #         return

        #     for temp_idx, word in enumerate(wordList[idx:]):
        #         if validate_diff(begin, word):
        #             recurse(word, end, idx + temp_idx + 1, wordList, count + 1)

        # recurse(beginWord, endWord, 0, wordList, 0)

        # return self.res


sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog"]

# beginWord = "a"
# endWord = "c"
# wordList = ["a","b","c"]

print sol.ladderLength(beginWord, endWord, wordList)
