class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        keys = set([])

        for s in A:
            keys.add(''.join(sorted(list(s[0::2])) + sorted(list(s[1::2]))))

        # base = ord('a')

        # for s in A:
        #     temp = [0] * 26

        #     for idx, c in enumerate(s):
        #         temp[ord(c) - base] = 1 if idx & 1 else 2
            
        #     keys.add(''.join(map(str, temp)))

        return len(keys)


sol = Solution()
# a = ["a","b","c","a","c","c"]
a = ["aa","bb","ab","ba"]
# a = ["ababaa","aaabaa"]
print(sol.numSpecialEquivGroups(a))
