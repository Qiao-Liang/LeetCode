class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left: left + k]

        # if not arr:
        #     return []

        # if x <= arr[0]:
        #     return arr[:k]
        
        # if x >= arr[-1]:
        #     return arr[-k:]

        # left = 0 
        # right = len(arr)

        # while left + 1 < right:
        #     mid = (left + right) // 2

        #     if arr[mid] < x:
        #         left = mid
        #     elif arr[mid] > x:
        #         right = mid
        #     else:
        #         break

        # while right - left <= k:
        #     if left == 0:
        #         return arr[:k]
        #     elif right == len(arr):
        #         return arr[-k:]
        #     else:
        #         if x - arr[left - 1] <= arr[right] - x:
        #             left -= 1
        #         else:
        #             right += 1

        # return arr[left: right]


sol = Solution()
arr = [1,2,3,4,5]
k = 4
x = 3

# arr = [1]
# k = 1
# x = 1

print(sol.findClosestElements(arr, k, x))
