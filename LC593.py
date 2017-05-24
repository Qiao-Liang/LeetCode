from itertools import combinations

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def square_dist(tup_p):
            return (tup_p[0][0] - tup_p[1][0]) ** 2 + (tup_p[0][1] - tup_p[1][1]) ** 2

        dist = sorted(list(map(square_dist, list(combinations([p1, p2, p3, p4], 2)))))

        return dist[0] > 0 and len(set(dist[:4])) == 1 and dist[4] == dist[5]
