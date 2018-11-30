class TrieNode():
    def __init__(self, char=None):
        self.char = char
        self.next = {}
        self.is_word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root

        for ch in word:
            if ch not in curr.next:
                curr.next[ch] = TrieNode(ch)

            curr = curr.next[ch]
        
        curr.is_word = True

    
    def _search(self, curr, word, is_prefix):
        for ch in word:
            if ch in curr.next:
                curr = curr.next[ch]
            else:
                return False

        return True if is_prefix else curr.is_word
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self._search(self.root, word, False)
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._search(self.root, prefix, True)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

trie = Trie()
trie.insert("apple")
print trie.search("apple")
print trie.search("app")
print trie.startsWith("app")
trie.insert("app")
print trie.search("app")
