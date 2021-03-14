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
        self.res = []

        def check(a, b):
            count = 0

            for ca, cb in zip(a, b):
                if ca != cb:
                    count += 1
                
            return count == 1

        for i, outer in enumerate(wordList):
            for inner in wordList[i + 1:]:
                if check(outer, inner):
                    next_words[outer].append(inner)
                    next_words[inner].append(outer)

        if endWord not in next_words:
            return []

        queue = [w for w in wordList if check(beginWord, w)]
        start = queue[:]
        depth = 2
        visited = set(queue)

        while True:
            temp = []
            cont = True
            depth += 1

            for w in queue:
                for nw in next_words[w]:
                    if nw == endWord:
                        cont = False

                    if nw not in visited:
                        visited.add(nw)
                        temp.append(nw)

            if cont:
                queue = temp
            else:
                break

        def dfs(word, path, visited):
            if len(path) < depth:
                for next_word in next_words[word]:
                    if next_word not in visited:
                        path.append(next_word)
                        visited.add(next_word)
                        
                        if next_word == endWord:
                            self.res.append(path[:])
                        else:
                            if not self.res or len(path) < len(self.res[0]):
                                dfs(next_word, path, visited)

                        path.pop()
                        visited.remove(next_word)

        for w in start:
            if w == endWord:
                return [[beginWord, endWord]]
            else:
                dfs(w, [beginWord, w], set([beginWord, w]))

        return self.res


sol = Solution()
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# beginWord = "a"
# endWord = "c"
# wordList = ["a", "b", "c"]
beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog","dot"]
# beginWord = "qa"
# endWord = "sq"
# wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
print(sol.findLadders(beginWord, endWord, wordList))
