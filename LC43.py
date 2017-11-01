class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        def single_multiply(str_num, digit):
            result = 0
            carry = 0

            for int(num) in str_num[::-1]:
                
