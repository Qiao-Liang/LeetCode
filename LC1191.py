class Solution:
    def kConcatenationMaxSum(self, arr, k):
        len_arr = len(arr)
        curr_max = global_max = 0

        for i in range(len_arr if k == 1 else len_arr * 2):
            n = arr[i % len_arr]
            curr_max = max(n, curr_max + n)
            global_max = max(global_max, curr_max)

        return (global_max + ((k - 2) * max(0, sum(arr)) if k > 1 else 0)) % (10 ** 9 + 7)


sol = Solution()
# p = [[1,2], 3]
p = [[1,-2,1], 5]
# p = [[-1,-2], 7]
# p = [[1, -1], 1]
# p = [[-5,-2,0,0,3,9,-2,-5,4],5]
print(sol.kConcatenationMaxSum(*p))
