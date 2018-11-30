# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
pick = 6

def guess(num):
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0
    

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            check = guess(mid)

            if check == 1:
                left = mid + 1
            elif check == -1:
                right = mid - 1
            else:
                return mid


sol = Solution()
print(sol.guessNumber(10))
