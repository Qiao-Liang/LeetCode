class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0

        len_words = len(words)
        keys = [0] * len_words
        base = ord('a')
        res = 0

        for idx, word in enumerate(words):
            temp = 0

            for ch in word:
                temp |= 1 << (ord(ch) - base)

            keys[idx] = temp

        for idx in xrange(len_words):
            for loop in xrange(idx + 1, len_words):
                if keys[idx] & keys[loop] == 0:
                    res = max(res, len(words[idx]) * len(words[loop]))

        return res


sol = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print sol.maxProduct(words)
