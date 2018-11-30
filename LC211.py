class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.trie
        parent = None
        
        for ch in word:
            if ch not in root:
                root[ch] = {}
            
            parent = root
            root = root[ch]

        if 'end' in parent:
            parent['end'].add(word[-1])
        else:
            parent['end'] = set([word[-1]])

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def recurse(root, chs, idx):
            if root and idx == len(chs) - 1:
                return 'end' in root and (chs[-1] in root['end'] or chs[-1] == '.')
            
            if not root:
                return False

            if chs[idx] in root:
                return recurse(root[chs[idx]], chs, idx + 1)

            if chs[idx] == '.':
                for key in root.keys():
                    if key != 'end':
                        if recurse(root[key], chs, idx + 1):
                            return True
                
                return False
            elif chs[idx] not in root:
                return False

        return recurse(self.trie, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")

print obj.trie
# print obj.search("pad")
# print obj.search("bad")
print obj.search(".ad")
# print obj.search("b..")
# print obj.search("b.d")

# print obj.search(".")
