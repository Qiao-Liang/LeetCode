class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        len_s = len(s)

        if len_s < 10:
            return []
        
        dic_count = {}

        for idx in xrange(len_s - 9):
            curr = s[idx: idx + 10]

            if curr in dic_count:
                dic_count[curr] += 1
            else:
                dic_count[curr] = 1

        # for outer in xrange(len_s - 9):
        #     curr = s[outer: outer + 10]

        #     if curr not in dic_count:
        #         dic_count[curr] = 1

        #         for inner in xrange(outer + 1, len_s - 9):
        #             if curr == s[inner: inner + 10]:
        #                 dic_count[curr] += 1
                
        #         if dic_count[curr] == 1:
        #             del dic_count[curr]

        return [key for key in dic_count.keys() if dic_count[key] > 1]


sol = Solution()
s = "AAAAACCCCCAAAAAGGGTTTAAAAACCCCCC"
# s = "AAAAAAAAAAA"
print sol.findRepeatedDnaSequences(s)
        