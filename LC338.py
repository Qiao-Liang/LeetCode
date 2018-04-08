class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        last_base = None
        next_base = 1
        curr_num = 1

        while curr_num <= num:
            if curr_num == next_base:
                res[curr_num] = 1
                last_base = curr_num
                next_base <<= 1
            else:
                res[curr_num] = 1 + res[curr_num - last_base]

            curr_num += 1

        return res


sol = Solution()
print sol.countBits(1)
