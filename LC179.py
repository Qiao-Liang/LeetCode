class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # def compare(a, b):
        #     str_a = str(a)
        #     str_b = str(b)
        #     len_a = len(str_a)
        #     len_b = len(str_b)
        #     idx_a = idx_b = 0

        #     if len_a == len_b:
        #         return a < b

        #     while idx_a < len_a and idx_b < len_b:
        #         if str_a[idx_a] == str_b[idx_b]:
        #             idx_a += 1
        #             idx_b += 1
        #         else:
        #             break

        #     if len_a > len_b:
        #         return str_a[idx_a] < str_b[idx_b - 1]
            
        #     if len_b > len_a:
        #         return str_b[idx_b] < str_a[idx_a - 1]

        # temp = sorted(nums, cmp = compare, reverse = True)

        def compare(x, y):
            x_y = x + y
            y_x = y + x

            if x_y < y_x:
                return 1
            elif x_y > y_x:
                return -1
            else:
                return 0

        return str(int(''.join(sorted(map(str, nums), cmp=compare))))


sol = Solution()
# nums = [3,30,34,5,9]
# nums = [30, 3]
nums = [0, 0, 0]
print sol.largestNumber(nums)
