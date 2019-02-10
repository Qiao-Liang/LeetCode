class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dic = {}

        for word in A.split(' '):
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

        for word in B.split(' '):
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

        return [key for key, val in dic.items() if val == 1]


sol = Solution()
# A = "this apple is sweet"
# B = "this apple is sour"

# A = "apple apple"
# B = "banana"

A = "s z z z s"
B = "s z ejt"
print(sol.uncommonFromSentences(A, B))
