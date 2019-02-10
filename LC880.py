class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0

        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size

            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size //= int(c)
            else:
                size -= 1



        # for ch in S:
        #     if ch in nums:
        #         temp_length = len(temp) * (int(ch) - 1)

        #         while temp_length > 0 and K > 0:
        #             K -= 1
        #             temp_length -= 1
        #             curr_idx += 1

        #         curr_idx %= len(temp)

        #         if K == 0:
        #             return temp[curr_idx]
        #     else:
        #         temp.append(ch)
        #         K -= 1
        #         curr_idx += 1

        #         if K == 0:
        #             return temp[curr_idx]


sol = Solution()
S = "leet2code3"
K = 10
# S = 'ha22'
# K = 5
# S = "a23"
# K = 6
# S = "a2b3c4d5e6f7g8h9"
# K = 9
print(sol.decodeAtIndex(S, K))
