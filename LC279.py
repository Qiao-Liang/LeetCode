class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        cands = []
        curr = 1

        while True:
            temp = curr ** 2

            if temp < n:
                cands.append(curr ** 2)
            elif temp == n:
                return 1
            else:
                break
            
            curr += 1

        res = 0
        queue = [n]

        while queue:
            temp_queue = []
            res += 1

            for num in queue:
                for cand in cands:
                    if cand < num:
                        temp_queue.append(num - cand)
                    elif cand == num:
                        return res
                    else:
                        break

            queue = temp_queue

        return res

    def numSquares2(self, n):
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


sol = Solution()
# print(sol.numSquares(1))

from time import time

t = time()
print(sol.numSquares2(7691))
print(time() - t)

t = time()
print(sol.numSquares(7691))
print(time() - t)
        