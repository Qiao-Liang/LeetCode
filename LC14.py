class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        min_len = min([len(s) for s in strs])
        result = ''

        for idx in range(min_len):
            first = strs[0][idx]
            diff = False
            for s in strs[1:]:
                if s[idx] != first:
                    diff = True
                    break
            
            if diff:
                break
            else:
                result += first

        return result


strs = ['abc', 'ab', 'abcd']
sol = Solution()
print(sol.longestCommonPrefix(strs))
