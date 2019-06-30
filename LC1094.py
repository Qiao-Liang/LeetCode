class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        queue = []
        curr_cap = 0
        trips.sort(key=lambda n: (n[1], n[2]))
        
        for psg, srt, end in trips:
            curr_cap += psg

            temp_queue = []
            for item in queue:
                if item[1] <= srt:
                    curr_cap -= item[0]
                else:
                    temp_queue.append(item)

            if curr_cap > capacity:
                return False

            queue = temp_queue
            queue.append((psg, end))
        
        return True


sol = Solution()
# params = [[[3,2,8],[4,4,6],[10,8,9]],11]
params = [[[2,2,6],[2,4,7],[8,6,7]],11]
# params = [[[7,5,6],[6,7,8],[10,1,6]],16]
# params = [[[9,3,4],[9,1,7],[4,2,4],[7,4,5]],23]
print(sol.carPooling(*params))
