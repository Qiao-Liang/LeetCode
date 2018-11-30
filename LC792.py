class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def is_subseq(w, s):
            w_idx = s_idx = 0
            len_w = len(w)
            len_s = len(s)

            while w_idx < len_w and s_idx < len_s:
                if w[w_idx] == s[s_idx]:
                    w_idx += 1
                    s_idx += 1
                else:
                    s_idx += 1

            return w_idx == len_w

        res = 0

        for word in words:
            if is_subseq(word, S):
                res += 1

        return res


sol = Solution()
S = "abcde"
words = ["a", "bb", "acd", "ace"]
print sol.numMatchingSubseq(S, words)
