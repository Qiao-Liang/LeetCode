class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = []

        while A or B:
            if len(res) > 1 and res[-1] == res[-2]:
                is_b = res[-1] == 'a'
            else:
                is_b = A < B

            if is_b:
                B -= 1
                res.append('b')
            else:
                A -= 1
                res.append('a')

        return ''.join(res)

        # self.res = None

        # def dfs(len_a, len_b, is_a, temp):
        #     if self.res:
        #         return

        #     if len_a < 0 or len_b < 0:
        #         return

        #     if len_a == 0 and len_b == 0:
        #         self.res = ''.join(temp)
        #         return

        #     if is_a:
        #         dfs(len_a - 1, len_b, not is_a, temp + ['a'])
        #         dfs(len_a - 2, len_b, not is_a, temp + ['aa'])
        #     else:
        #         dfs(len_a, len_b - 1, not is_a, temp + ['b'])
        #         dfs(len_a, len_b - 2, not is_a, temp + ['bb'])

        # dfs(A, B, A > B, [])
        # return self.res


sol = Solution()
a = 100
b = 82
print(sol.strWithout3a3b(a, b))
        