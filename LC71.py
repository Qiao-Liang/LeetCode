class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_arr = [d for d in path.split('/') if d != '' and d != '.']
        result = []
        count = 0

        while path_arr:
            while path_arr and path_arr[-1] == '..':
                path_arr.pop()
                count += 1

            while path_arr and count > 0:
                if path_arr[-1] == '..':
                    break
                else:
                    path_arr.pop()
                    count -= 1

            if path_arr and path_arr[-1] != '..':
                result.append(path_arr.pop())

        return '/' + '/'.join(reversed(result))


sol = Solution()
# path = "/a/./b/../../c/"
# path = "/a//b////c/d//././/.."
# path = '/..'
path = "/home/of/foo/../../bar/../../is/./here/."
print sol.simplifyPath(path)
        