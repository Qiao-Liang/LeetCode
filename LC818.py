class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        queue = [(0, 1)]
        res = 0
        visited = set([])
        bound = target << 1

        while True:
            temp_queue = []
            res += 1

            for pos, spd in queue:
                if pos == target or pos + spd == target:
                    return res

                temp1 = (pos + spd, spd << 1)
                temp2 = (pos, 1 if spd < 0 else -1)

                if temp1[0] < bound and temp1[1] < bound and temp1 not in visited:
                    visited.add(temp1)
                    temp_queue.append(temp1)

                if temp2 not in visited:
                    visited.add(temp2)
                    temp_queue.append(temp2)
            
            queue = temp_queue


sol = Solution()
print(sol.racecar(4))
