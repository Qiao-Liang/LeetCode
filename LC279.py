class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = [0] * (n + 1)
        sqr_nums = [0, 1]

        for num in range(1, n + 1):
            if num == sqr_nums[-1]:
                counts[num] = 1
                sqr_nums.append(len(sqr_nums) ** 2)
            else:
                count = (num / sqr_nums[-2]) * counts[sqr_nums[-2]] + counts[num % sqr_nums[-2]]
                for sqr in sqr_nums[1:-1]:
                    count = min(count, (num / sqr) * counts[sqr] + counts[num % sqr])

                counts[num] = count

        return counts[-1]


from time import time
sol = Solution()
t = time()
print(sol.numSquares(7691))
print(time() - t)
        