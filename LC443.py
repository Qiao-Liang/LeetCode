class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return None

        last = chars[0]
        border = 0
        count = 1

        for idx in xrange(1, len(chars)):
            if chars[idx] == last:
                count += 1
            else:
                chars[border] = last

                if count > 1:
                    for ch in str(count):
                        border += 1
                        chars[border] = ch
                    
                border += 1
                last = chars[idx]
                count = 1

        chars[border] = last

        if count > 1:
            for ch in str(count):
                border += 1
                chars[border] = ch

        return border + 1


sol = Solution()
# chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print sol.compress(chars)
