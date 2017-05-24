from re import findall
from functools import reduce


class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def get_gcd(n1, n2):
            return get_gcd(n2, n1 % n2) if n2 > 0 else n1
        
        def get_lcm(n1, n2):
            return n1 * n2 // get_gcd(n1, n2)
        
        operands = [int(n) for n in findall('-?\d+', expression)]

        numerator = operands[1]
        count = 3
        while count < len(operands):
            numerator = get_lcm(numerator, operands[count])
            count += 2
        
        fractions = []
        count = 0
        while count < len(operands):
            fractions.append(operands[count] * numerator // operands[count + 1])
            count += 2

        fraction = reduce((lambda x, y: x + y), fractions)
        gcd = get_gcd(fraction, numerator)

        return str(fraction // gcd) + '/' + str(numerator // gcd)
