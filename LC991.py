class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        if Y <= X:
            return X - Y

        res = 0

        while Y > X:
            res += 1

            if Y & 1:
                Y += 1
            else:
                Y >>= 1

        return res + X - Y

        # while X << 1 < Y:
        #     X <<= 1

        # queue = [X]
        # go_on = True

        # while go_on:
        #     res += 1
        #     temp_queue = []

        #     for n in queue:
        #         sub = n - 1
        #         double = n << 1

        #         if sub == Y or double == Y:
        #             go_on = False
        #             break

        #         temp_queue.append(sub)
        #         temp_queue.append(double)

        #     queue = temp_queue

        # return res


sol = Solution()
X = 1
Y = 10000
print(sol.brokenCalc(X, Y))
