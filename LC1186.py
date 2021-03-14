class Solution:
    def maximumSum(self, arr) -> int:
        len_arr = len(arr)
        forward = [0] * len_arr
        backward = [0] * len_arr
        curr = max_val = forward[0] = arr[0]

        for i, n in enumerate(arr[1:], start=1):
            curr = max(n, curr + n)
            max_val = max(max_val, curr)
            forward[i] = curr

        curr = max_val = backward[-1] = arr[-1]

        for i in range(len_arr - 2, -1, -1):
            curr = max(arr[i], curr + arr[i])
            max_val = max(max_val, curr)
            backward[i] = curr

        res = max_val

        for i in range(1, len_arr - 1):
            res = max(res, forward[i - 1] + backward[i + 1])

        return res


sol = Solution()
# arr = [1, -2, 0, 3]
# arr = [1, -2, -2, 3]
arr = [-1,-1,-1,-1]
print(sol.maximumSum(arr))
