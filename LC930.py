class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        i_lo = i_hi = 0
        temp_sum = 0
        ans = 0

        for j, x in enumerate(A):
            temp_sum += x

            # Maintain i_lo, temp_sum:
            # Increase i_lo until temp_sum equals to the target sum
            while i_lo < j and temp_sum > S:
                temp_sum -= A[i_lo]
                i_lo += 1

            i_hi = i_lo

            # Maintain i_hi, sum_hi:
            # Increase i_hi starting from i_lo while A[i_hi] is 0
            while i_hi < j and not A[i_hi]:
                i_hi += 1

            if temp_sum == S:
                ans += i_hi - i_lo + 1

        return ans

        # from collections import Counter
        # c = Counter({0: 1})
        # psum = res = 0

        # for i in A:
        #     psum += i
        #     res += c[psum - S]
        #     c[psum] += 1

        # return res


sol = Solution()
# a = [1,0,1,0,1]
# s = 2
a = [0, 0, 0, 0, 0]
s = 0
print(sol.numSubarraysWithSum(a, s))
