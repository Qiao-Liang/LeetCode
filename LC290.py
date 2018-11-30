class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic_ptn = {}
        str_list = str.split(' ')

        if len(pattern) != len(str_list):
            return False

        for idx, ptn in enumerate(pattern):
            if ptn in dic_ptn:
                dic_ptn[ptn].append(idx)
            else:
                dic_ptn[ptn] = [idx]

        for vals in dic_ptn.values():
            temp = str_list[vals[0]]

            for val in vals:
                if temp != str_list[val]:
                    return False

        return len(dic_ptn.keys()) == len(set(str_list))


sol = Solution()
# pattern = "abba"
# txt = "dog cat cat dog"
pattern = "jquery"
txt = "jquery"
print sol.wordPattern(pattern, txt)
