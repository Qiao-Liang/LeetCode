class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        heights.append(0)
        max_rec = 0
        min_stk = [-1]

        for idx, val in enumerate(heights):
            while val < heights[min_stk[-1]]:
                max_rec = max(max_rec, heights[min_stk.pop()] * (idx - min_stk[-1] - 1))        

            min_stk.append(idx)

        return max_rec

        # len_hgt = len(heights)
        # max_rec = heights[0]

        # for idx in range(1, len_hgt):
        #     temp_max = last_min = heights[idx]
        #     temp_idx = idx - 1
        #     temp = []

        #     while temp_idx > -1:
        #         if heights[temp_idx] < last_min:
        #             last_min = heights[temp_idx]
        #             temp.append(temp_idx)
                
        #         temp_max = max(temp_max, (idx - temp_idx + 1) * last_min)
        #         temp_idx -= 1

        #     print(idx, temp)
        #     max_rec = max(temp_max, max_rec)

        # return max_rec


sol = Solution()
m = [2,1,5,6,2,3]
# m = [2,1,1,1,2,3]
# m = []
print(sol.largestRectangleArea(m))
