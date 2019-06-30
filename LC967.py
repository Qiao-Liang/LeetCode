class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        res = {n for n in range(1, 10)}

        for _ in range(N - 1):
            temp = set([])
            
            for n in res:
                d = n % 10
                n *= 10

                if d + K < 10:
                    temp.add(n + d + K)
                
                if d - K > -1:
                    temp.add(n + d - K)
            
            res = temp

        if N == 1:
            res.add(0)

        return list(res)


        # self.res = set([])
        # bound = (10 ** (N - 1)) if N > 1 else 0
        # ch_low_bound = ord('0')
        # ch_up_bound = ord('9')
        
        # def recurse(str_num):
        #     if len(str_num) == N:
        #         num = int(str_num[::-1])

        #         if num >= bound:
        #             self.res.add(num)
        #     else:
        #         digit_ord = ord(str_num[-1])

        #         if digit_ord + K <= ch_up_bound:
        #             recurse(str_num + chr(digit_ord + K))

        #         if digit_ord - K >= ch_low_bound:
        #             recurse(str_num + chr(digit_ord - K))
            
        # for n in range(10):
        #     recurse(str(n))
        
        # return list(self.res)


sol = Solution()
# params = [3, 7]
# params = [2, 1]
# params = [1, 0]
params = [2, 0]
print(sol.numsSameConsecDiff(*params))
