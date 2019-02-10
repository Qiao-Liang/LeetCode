class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp = sorted([(val, idx) for idx, val in enumerate(A)], key=lambda x: (x[0], x[1]))
        bound = len(temp) - 1
        end = A[-1]
        res = 0

        def bin_search(target):
            left = 0
            right = bound

            while left <= right:
                mid = (left + right) // 2

                if temp[mid][0] > target:
                    right = mid - 1
                elif temp[mid][0] < target:
                    left = mid + 1
                else:
                    while mid > 0 and temp[mid - 1][0] == temp[mid][0]:
                        mid -= 1
                    
                    return mid

        for num in A[:-1]:
            target = num
            smaller = False
            left = 0
            right = bound

            while True:
                temp_idx = bin_search(target)

                if smaller:
                    if temp_idx > left:
                        right = temp_idx - 1
                        target = temp[right][0]
                    else:
                        break
                else:
                    if temp_idx < right:
                        left = temp_idx + 1
                        target = temp[left][0]
                    else:
                        break

                if target == end:
                    res += 1
                    break

                smaller = not smaller

        return res + 1


sol = Solution()
# a = [10,13,12,14,15]
# a = [2,3,1,1,4]
a = [5,1,3,4,2]
print(sol.oddEvenJumps(a))
        