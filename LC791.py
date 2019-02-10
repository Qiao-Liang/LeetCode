class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic_t = {}
        res = []

        for ch in T:
            if ch in dic_t:
                dic_t[ch] += 1
            else:
                dic_t[ch] = 1

        for ch in S:
            if ch in dic_t:
                res.append(ch * dic_t[ch])
                del dic_t[ch]

        for key, val in dic_t.items():
            res.append(key * val)

        return ''.join(res)

        # set_s = set(list(S))
        # set_t = set(list(T))
        # temp_t = []
        # temp_s = []

        # for ch in T:
        #     if ch not in set_s:
        #         temp_t.append(ch)

        # for ch in S:
        #     if ch in set_t:
        #         temp_s.append(ch)

        # return ''.join(temp_s + temp_t)


sol = Solution()
# S = "cba"
# T = "abcd"
# S = "cbafg"
# T = "abcd"
S = "kqep"
T = "pekeq"
print(sol.customSortString(S, T))
