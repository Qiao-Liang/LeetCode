class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stat_dict = {}
        base = ord('a')
        result = []

        for idx, c in enumerate(s):
            temp_ord = ord(c) - base

            if temp_ord in stat_dict:
                stat_dict[temp_ord].append(idx)
            else:
                stat_dict[temp_ord] = [idx]

        while stat_dict:
            keys = sorted(stat_dict.keys())

            for key in keys:
                for oth_key in keys:
                    if stat_dict[key][0] > stat_dict[oth_key][-1]:
                        break
                else:
                    result.append(chr(key + base))
                    last_idx = stat_dict[key][0]
                    del stat_dict[key]

                    for key in stat_dict:
                        stat_dict[key] = [n for n in stat_dict[key] if n > last_idx]

                    break
                
        return ''.join(result)


sol = Solution()
print(sol.removeDuplicateLetters("cbacdcbc"))
