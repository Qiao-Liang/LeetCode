class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        self.res = 0

        def is_square(x, y):
            temp_sum = x + y

            if temp_sum == 0:
                return True
            else:
                high = 1

                while high ** 2 < temp_sum:
                    high <<= 1

                low = high >> 1

                while low <= high:
                    mid = (low + high) // 2
                    sqr_mid = mid ** 2

                    if sqr_mid > temp_sum:
                        high = mid - 1
                    elif sqr_mid < temp_sum:
                        low = mid + 1
                    else:
                        return True

                return False

        def permute(arr, left, right):
            if left == right - 1: #and is_square(arr[left], arr[left - 1]):
                print(arr)
                # self.res += 1
            else:
                for idx in range(left, right):
                    arr[left], arr[idx] = arr[idx], arr[left]

                    if is_square(arr[left], arr[left + 1]):
                        permute(arr, left + 1, right)
    
                    arr[left], arr[idx] = arr[idx], arr[left]

        permute(A, 0, len(A))
        return self.res


sol = Solution()
a = [1, 17, 8]
print(sol.numSquarefulPerms(a))
