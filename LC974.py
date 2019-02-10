class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        rem_dic = {}
        rem_dic[0] = 1
        temp_sum = res = 0

        for num in A:
            temp_sum += num
            temp_rem = temp_sum % K
            
            if temp_rem in rem_dic:
                res += rem_dic[temp_rem]
                rem_dic[temp_rem] += 1
            else:
                rem_dic[temp_rem] = 1

        return res

        # len_A = len(A)
        # temp = [[0] * len_A for _ in range(len_A)]
        # res = 0

        # for idx, val in enumerate(A):
        #     temp[idx][idx] = val
            
        #     if val % K == 0:
        #         res += 1

        # for row in range(len_A):
        #     for col in range(row + 1, len_A):
        #         temp[row][col] = temp[row][col - 1] + temp[col][col]

        #         if temp[row][col] % K == 0:
        #             res += 1

        # return res


sol = Solution()
A = [4,5,0,-2,-3,1]
K = 5
print(sol.subarraysDivByK(A, K))
        