class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A or len(A) == 1:
            return True

        temp = A[0]
        func = None

        for num in A[1:]:
            if func:
                if func(temp, num):
                    temp = num
                else:
                    return False
            else:
                if temp > num:
                    temp = num
                    func = lambda x, y: x >= y
                elif temp < num:
                    temp = num
                    func = lambda x, y: x <= y
                else:
                    continue

        return True


sol = Solution()
# a = [6,5,4,4]
# a = [1,3,2]
# a = [1, 1, 1]
# a = [1, 2, 2, 3]
# a = [5,3,2,4,1]
# a = [1,1,0]
print(sol.isMonotonic(a))
        