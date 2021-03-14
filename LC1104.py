class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        tree = [1]
        reverse = True
        num = 2
        length = 2
        res = [label]
        
        while True:
            temp = [n for n in range(num, num + length)]
            
            if reverse:
                temp.reverse()
            
            tree.extend(temp)
            reverse = not reverse
            num += length
            length <<= 1

            if num > label:
                break
        
        idx = tree.index(label)
        
        while idx > 0:
            if idx & 1:
                idx = (idx - 1) // 2
            else:
                idx = (idx - 2) // 2
                
            res.append(tree[idx])
            
        return res[::-1]

        # tree = []
        # last = [1]
        # reverse = True
        # num = 1
        # res = [label]
        
        # while num < label:
        #     tree.extend(last)
        #     temp_last = []
            
        #     for _ in last:
        #         num += 1
        #         temp_last.append(num)
        #         num += 1
        #         temp_last.append(num)
            
        #     last = temp_last
            
        #     if reverse:
        #         last.reverse()
                
        #     reverse = not reverse
        
        # tree.extend(last)
        # idx = tree.index(label)
        
        # while idx > 0:
        #     if idx & 1:
        #         idx = (idx - 1) // 2
        #     else:
        #         idx = (idx - 2) // 2
                
        #     res.append(tree[idx])
            
        # return res[::-1]

    def pathInZigZagTree2(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        # result = []
        # bit_pos = len(bin(label)) - 2
        # is_odd_bit = bit_pos % 2
        # while bit_pos > 0:
        #     pos = label - 2 ** (bit_pos-1)
        #     if bit_pos % 2 != is_odd_bit:
        #         result.insert(0, 2 ** bit_pos - 1 - pos)
        #     else:
        #         result.insert(0, 2 ** (bit_pos - 1) + pos)
        #     label = label // 2
        #     bit_pos -= 1
        # return result

        bit_len = len(bin(label)) - 2
        res = [None] * bit_len
        idx = -1
        is_odd = bit_len & 1
        lo = 2 ** (bit_len - 1)
        hi = lo << 1

        while bit_len > 0:
            pos = label - lo

            if bit_len & 1 == is_odd:
                res[idx] = lo + pos
            else:
                res[idx] = hi - 1 - pos

            idx -= 1
            bit_len -= 1
            label >>= 1
            lo >>= 1
            hi >>= 1

        return res


sol = Solution()
l = 16
print(sol.pathInZigZagTree2(l))
        