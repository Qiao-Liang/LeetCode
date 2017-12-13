class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = map(lambda x: int(x), list(reduce(lambda x, y: x + y, time.split(':'))))
        mini = min(digits)
        template = '{0}{1}:{2}{3}'

        next_digit = min([n for n in digits[:3] if n > digits[3]] or [-1])
        if next_digit != -1 and digits[2] * 10 + next_digit < 60:
            return template.format(digits[0], digits[1], digits[2], next_digit)

        next_digit = min([n for n in digits[:2] + digits[3:] if n > digits[2]] or [-1])
        if next_digit != -1 and next_digit * 10 + mini < 60:
            return template.format(digits[0], digits[1], next_digit, mini)

        next_digit = min([n for n in digits[:1] + digits[2:] if n > digits[1]] or [-1])
        if next_digit != -1 and digits[0] * 10 + next_digit < 24:
            return template.format(digits[0], next_digit, mini, mini)

        next_digit = min([n for n in digits[1:] if n > digits[0]] or [-1])
        if next_digit != -1 and next_digit * 10 + digits[1] < 24:
            return template.format(next_digit, mini, digits[2], digits[3])
        
        return template.format(mini, mini, mini, mini)


sol = Solution()
print(sol.nextClosestTime('13:55'))
            