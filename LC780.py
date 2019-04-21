class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx >= sx and ty >= sy:
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            elif tx < ty:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
            else:
                break
        
        return sx == tx and sy == ty


        # while tx >= 0 and ty >= 0:
        #     if sx == tx and sy == ty:
        #         return True

        #     if tx > ty:
        #         tx -= ty
        #     else:
        #         ty -= tx

        # return False


        # queue = [(sx, sy)]

        # while queue:
        #     temp_queue = []

        #     for x, y in queue:
        #         if x == tx and y == ty:
        #             return True
            
        #         temp = x + y

        #         if temp <= tx:
        #             temp_queue.append((temp, y))
                
        #         if temp <= ty:
        #             temp_queue.append((x, temp))

        #     queue = temp_queue

        # return False


sol = Solution()
sx = 3
sy = 3
tx = 12
ty = 9
print(sol.reachingPoints(sx, sy, tx, ty))
