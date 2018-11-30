class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dic = {}
        mapped = set([])
        for s_ch, t_ch in zip(s, t):
            if s_ch not in dic:
                if t_ch in mapped:
                    return False
                else:
                    dic[s_ch] = t_ch
                    mapped.add(t_ch)
            elif dic[s_ch] != t_ch:
                    return False

        return True

        # len_s = len(s)
        # len_t = len(t)

        # if len_s != len_t:
        #     return False

        # def get_pattern(txt, len_txt):
        #     ptrn = [0] * len_txt
        #     dic = {}

        #     for idx in xrange(len_txt):
        #         if txt[idx] not in dic:
        #             dic[txt[idx]] = idx

        #         ptrn[idx] = dic[txt[idx]]

        #     return ptrn

        # ptrn_s = get_pattern(s, len_s)
        # ptrn_t = get_pattern(t, len_t)

        # for idx in xrange(len_s):
        #     if ptrn_s[idx] != ptrn_t[idx]:
        #         return False

        # return True


sol = Solution()
# s = 'egg'
# t = 'add'
# s = "foo"
# t = "bar"
# s = "paper"
# t = "title"
s = "ab"
t = "aa"

print(sol.isIsomorphic(s, t))
        