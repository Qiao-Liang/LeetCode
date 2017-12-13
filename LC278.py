# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 1

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n

        while left <= right:
            mid = (left + right) / 2

            if isBadVersion(mid):
                if mid == 0:
                    return 0
                else:
                    if isBadVersion(mid - 1):
                        right = mid - 1
                    else:
                        return mid
            else:
                left = mid + 1


sol = Solution()
print(sol.firstBadVersion(1))
