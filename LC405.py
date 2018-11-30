class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        count = base = temp = group = 0

        while count < 33:
            if group == 4:
                res.append(dic[temp])
                base = temp = group = 0

            temp += (num & 1) << base
            num >>= 1
            base += 1
            count += 1
            group += 1
        
        while res and res[-1] == '0':
            res.pop()

        return ''.join(reversed(res)) if res else '0'


sol = Solution()
print sol.toHex(-1)
        