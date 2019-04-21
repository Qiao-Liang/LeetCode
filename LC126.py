from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        next_words = defaultdict(list)

        for outer in wordList:
            for inner in wordList:
                count = 0

                for ch_o, ch_i in zip(outer, inner):
                    if ch_o != ch_i:
                        count += 1
                
                if count == 1:
                    next_words[outer].append(inner)

        if beginWord not in next_words:
            for word in wordList:
                count = 0

                for ch_b, ch_w in zip(beginWord, word):
                    if ch_b != ch_w:
                        count += 1

                if count == 1:
                    next_words[beginWord].append(word)

        if endWord in next_words[beginWord]:
            return [[beginWord, endWord]]

        self.res = []

        def dfs(word, path, visited):
            if word not in next_words:
                return

            for next_word in next_words[word]:
                if next_word not in visited:
                    path.append(next_word)
                    visited.add(next_word)
                    
                    if next_word == endWord:
                        if self.res:
                            if len(path) < len(self.res[0]):
                                self.res = [path[:]]
                            elif len(path) == len(self.res[0]):
                                self.res.append(path[:])
                        else:
                            self.res = [path[:]]
                    else:
                        dfs(next_word, path, visited)

                    path.pop()
                    visited.remove(next_word)

        for next_word in next_words[beginWord]:
            dfs(next_word, [beginWord, next_word], set([beginWord, next_word]))

        return self.res


sol = Solution()
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = "a"
# endWord = "c"
# wordList = ["a", "b", "c"]
# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog","dot"]
beginWord = "qa"
endWord = "sq"
wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
print(sol.findLadders(beginWord, endWord, wordList))
