class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        elif n == 1:
            return ['()']
        else:
            result = {1: {'()': ''}}
            curr = 2
            
            while curr <= n:
                temp = {}
                for key in result[curr - 1]:
                    mid = '({})'.format(key)
                    left = '(){}'.format(key)
                    right = '{}()'.format(key)

                    if mid not in temp:
                        temp[mid] = ''
                    if left not in temp:
                        temp[left] = ''
                    if right not in temp:
                        temp[right] = ''

                if curr > 3:
                    mid = curr / 2

                    inner = 2
                    while inner <= mid:
                        for l_key in result[inner]:
                            for r_key in result[curr - inner]:
                                l_opt = '{}{}'.format(l_key, r_key)
                                r_opt = '{}{}'.format(r_key, l_key)

                                if l_opt not in temp:
                                    temp[l_opt] = ''
                                if r_opt not in temp:
                                    temp[r_opt] = ''
                        
                        inner += 1

                result[curr] = temp
                curr += 1
        
            return result[n].keys()

sol = Solution()
print(sol.generateParenthesis(4))
