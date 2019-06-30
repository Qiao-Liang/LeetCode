class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        bound = N + 1
        queue = [1, 6, 8, 9]
        res = 0

        def rotate(num):
            temp = 0

            while num:
                digit = num % 10
                num //= 10

                if digit == 6:
                    digit = 9
                elif digit == 9:
                    digit = 6

                temp *= 10
                temp += digit

            return temp

        while queue:
            num = queue.pop(0)

            if num < bound:
                if rotate(num) != num:
                    res += 1

                num *= 10
                queue.extend([num, num + 1, num + 6, num + 8, num + 9])
            else:
                break

        return res
    
    def confusingNumberII2(self, N):
        """
        :type N: int
        :rtype: int
        """
        rots = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        nexts = {'0': '1', '1': '6', '6': '8', '8': '9', '9': '0'}
        num = ['0']
        bound = N + 1
        res = 0

        while True:
            idx = len(num) - 1

            while idx > -1:
                num[idx] = nexts[num[idx]]

                if num[idx] == '0':
                    idx -= 1
                else:
                    break
            
            if num[0] == '0':
                num.insert(0, '1')

            str_num = ''.join(num)

            if int(str_num) < bound:
                temp_set = set(num)

                if len(temp_set) == 1 and ('1' in temp_set or '8' in temp_set):
                    pass
                else:
                    temp = num[::-1]
                    
                    for idx, ch in enumerate(temp):
                        temp[idx] = rots[ch]

                    if int(''.join(temp)) != int(str_num):
                        res += 1
            else:
                break

        return res


        # res = 0
        # rots = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        # next_rots = {'2': '6', '3': '6', '4': '6', '5': '6', '7': '8'}
        # num = 1
        # bound = N + 1
        
        # while num < bound:
        #     str_num = str(num)
        #     temp = []
        #     valid = True
        #     idx = len(str_num) - 1
            
        #     while idx > -1:
        #         if str_num[idx] in rots:
        #             temp.append(rots[str_num[idx]])
        #         else:
        #             valid = False
        #             list_num = list(str_num)

        #             for idx, ch in enumerate(list_num):
        #                 if ch in next_rots:
        #                     list_num[idx] = next_rots[ch]

        #             num = int(''.join(list_num))
        #             break
                
        #         idx -= 1
            
        #     if valid:
        #         if int(''.join(temp)) != num:
        #             res += 1
            
        #         num += 1
        
        # return res


sol = Solution()
# n = 20
n = 1000000000
# n = 1999909
print(sol.confusingNumberII(n))
# print(sol.confusingNumberII2(n))
