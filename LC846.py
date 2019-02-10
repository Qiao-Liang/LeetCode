class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        len_hand = len(hand)

        if len_hand % W != 0:
            return False

        dic = {}

        for num in hand:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        keys = sorted(dic.keys())
        len_keys = len(keys)
        idx = 0

        while idx < len_keys:
            while dic[keys[idx]]:
                offset = 1
                dic[keys[idx]] -= 1

                while offset < W:
                    temp_key = keys[idx] + offset

                    if temp_key in dic and dic[temp_key]:
                        dic[temp_key] -= 1
                    else:
                        return False

                    offset += 1

            idx += 1
        
        return True


sol = Solution()
# hand = [1,2,3,6,2,3,4,7,8]
# hand = [2,2,2,2,2,2]
hand = [1,1,2,2,3,3]
W = 3
# hand = [5, 1]
# W = 2
print(sol.isNStraightHand(hand, W))
