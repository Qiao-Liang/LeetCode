class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def get_idx_pattern(s):
            dic = {}

            for idx, ch in enumerate(s):
                if ch in dic:
                    dic[ch].append(idx)
                else:
                    dic[ch] = [idx]

            return sorted(dic.values())

        idx_pattern = get_idx_pattern(pattern)
        res = []

        for word in words:
            if idx_pattern == get_idx_pattern(word):
                res.append(word)

        return res


sol = Solution()
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
print(sol.findAndReplacePattern(words, pattern))
