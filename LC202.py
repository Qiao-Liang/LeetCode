class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exist_nums = set([])

        while n != 1:
            if n in exist_nums:
                return False
            
            temp = 0
            exist_nums.add(n)

            while n > 0:
                temp += (n % 10) ** 2
                n //= 10

            n = temp
        
        return True

        # old_nums = []

        # while n != 1:
        #     if n in old_nums:
        #         return False

        #     temp_sum = 0
        #     old_nums.append(n)

        #     while n > 9:
        #         temp_sum += (n % 10) ** 2
        #         n = n / 10

        #     temp_sum += n ** 2
        #     n = temp_sum

        # return True


sol = Solution()
print(sol.isHappy(20))
