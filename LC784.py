class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        idx_map = [idx for idx, ch in enumerate(S) if ch.isalpha()]
        bitmap = 0
        bound = 1 << len(idx_map)
        
        while bitmap < bound:
            temp = list(S)
            bit_mask = 1
            # map_idx = -1

            # while bit_mask < bound:
            #     ch_idx = idx_map[map_idx]
            #     temp[ch_idx] = temp[ch_idx].upper() if bit_mask & bitmap else temp[ch_idx].lower()
            #     bit_mask <<= 1
            #     map_idx -= 1

            for i in idx_map:
                temp[i] = temp[i].upper() if bit_mask & bitmap else temp[i].lower()
                bit_mask <<= 1
            
            bitmap += 1
            res.append(''.join(temp))

        return res

    # def letterCasePermutation(self, S):
    #     """
    #     :type S: str
    #     :rtype: List[str]
    #     """
    #     idx_map = []
    #     res = []

    #     for idx, ch in enumerate(S):
    #         if ch.isalpha():
    #             idx_map.append(idx)

    #     len_idx = len(idx_map)
    #     bitmap = [0] * len_idx
    #     bound = 2 ** len_idx
    #     count = 0
        
    #     while count < bound:
    #         count += 1
    #         carry = 1
    #         idx = len_idx - 1
    #         temp = list(S)

    #         for ch_idx, bit in zip(idx_map, bitmap):
    #             if bit:
    #                 temp[ch_idx] = temp[ch_idx].upper()
    #             else:
    #                 temp[ch_idx] = temp[ch_idx].lower()
            
    #         res.append(''.join(temp))

    #         while idx > -1 and carry:
    #             new_carry = bitmap[idx] & carry
    #             bitmap[idx] ^= carry
    #             carry = new_carry
    #             idx -= 1

    #     return res


sol = Solution()
S = "a1b2"
# S = "3z4"
# S = "12345"
print(sol.letterCasePermutation(S))
