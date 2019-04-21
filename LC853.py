class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        times = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        res = 0

        while len(times) > 1:
            lead = times.pop()

            if lead < times[-1]:
                res += 1
            else:
                times[-1] = lead

        return res + len(times)

        # stack = [[pos, spd] for pos, spd in zip(position, speed)]
        # stack.sort(key=lambda n: n[0])
        # res = 0

        # while stack:
        #     temp_stack = []

        #     print(stack)

        #     for car in stack:
        #         car[0] += car[1]

        #     while stack:
        #         temp = stack.pop()

        #         while stack and (temp[0] < stack[-1][0] or temp[0] == stack[-1][0] == target):
        #             stack.pop()
                
        #         if temp[0] < target:
        #             temp_stack.append(temp)
        #         else:
        #             res += 1

        #     if len(temp_stack) == 1:
        #         return res + 1
            
        #     temp_stack.reverse()
        #     stack = temp_stack

        #     print(res)
        #     print('*' * 30)

        # return res


sol = Solution()
params = [
    # [12,
    # [10,8,0,5,3],
    # [2,4,1,1,3]],
    # [10,
    # [0,4,2],
    # [2,1,3]],
    # [13,
    # [10,2,5,7,4,6,11],
    # [7,5,10,5,9,4,1]],
    # [31,
    # [5,26,18,25,29,21,22,12,19,6],
    # [7,6,6,4,3,4,9,7,6,4]],
    # [21,
    # [1,15,6,8,18,14,16,2,19,17,3,20,5],
    # [8,5,5,7,10,10,7,9,3,4,4,10,2]],
    # [44,
    # [10,43,34,4,9,35,29,5,3,2,1,41,38,6],
    # [6,5,1,1,7,1,10,3,9,8,2,9,5,10]],
    [10,
    [6,8],
    [3,2]]
]

for param in params:
    print(sol.carFleet(*param))
