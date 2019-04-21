class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        res = 0
        len_points = len(points)

        for idx0, (x0, y0) in enumerate(points[:len_points - 2]):
            for idx1, (x1, y1) in enumerate(points[idx0 + 1: len_points - 1], start=idx0 + 1):
                for x2, y2 in points[idx1 + 1:]:
                    res = max(res, 0.5 * abs(x0 * (y1 - y2) + x1 * (y2 - y0) + x2 * (y0 - y1)))

        return res

        # len_points = len(points)

        # for idx0 in range(len_points - 2):
        #     for idx1 in range(idx0 + 1, len_points - 1):
        #         for idx2 in range(idx0 + 2, len_points):
        #             (x1, y1), (x2, y2), (x3, y3) = points[idx0], points[idx1], points[idx2]

        #             res = max(res, 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        # return res
