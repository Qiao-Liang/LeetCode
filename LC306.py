class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        self.num = num
        self.bound = len(num)

        def dfs(start_idx, prev_nums):
            if start_idx == self.bound:
                return False

            if len(prev_nums) == 2:
                temp_sum = sum(prev_nums)
                str_sum = str(temp_sum)
                temp_bound = start_idx + len(str_sum)

                if self.num[start_idx: temp_bound] == str_sum:
                    if temp_bound == self.bound:
                        return True
                    else:
                        return dfs(temp_bound, [prev_nums[1], temp_sum])
                else:
                    return False
            else:
                for temp_start in xrange(start_idx + 1, self.bound):
                    prev_nums.append(int(self.num[start_idx: temp_start]))

                    if dfs(temp_start, prev_nums):
                        prev_nums.pop()
                        return True
                    
                    prev_nums.pop()

                    if num[start_idx: temp_start] == '0':
                        break

            return False

        return dfs(0, [])


sol = Solution()
print sol.isAdditiveNumber("199100199")
