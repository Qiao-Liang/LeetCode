class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ['1']

        while n > 1:
            last = res[0]
            count = 1
            temp = []

            for c in res[1:]:
                if c == last:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(last)
                    count = 1
                    last = c

            temp.append(str(count))
            temp.append(last)
            res = temp
            n -= 1

        return ''.join(res)


sol = Solution()
print sol.countAndSay(4)
