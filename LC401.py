class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 8:
            return []

        if num == 0:
            return ["0:00"]

        map = [0] * 11
        map[1] = map[5] = 1
        for idx in xrange(2, 5):
            map[idx] = map[idx - 1] << 1

        for idx in xrange(6, 11):
            map[idx] = map[idx - 1] << 1

        combines = []
        stack = []
        curr = 1
        space = 10 - num + 1
        result = []

        while True:
            len_stk = len(stack)

            if len_stk == num or curr > space + len_stk:
                if not stack:
                    break
                
                if len_stk == num:
                    combines.append(stack[:])
                
                curr = stack.pop() + 1
            else:
                stack.append(curr)
                curr += 1

        for combine in combines:
            hours = sum([map[idx] for idx in combine if idx < 5])
            mins = sum([map[idx] for idx in combine if idx > 4])

            if hours < 12 and mins < 60:
                result.append("{0}:{1}".format(hours, mins if mins > 9 else '0' + str(mins)))

        return result


sol = Solution()
print sol.readBinaryWatch(2) 
