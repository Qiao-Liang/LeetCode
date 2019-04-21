class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []

        self.temp_list = []
        self.res = None
        self.bound = len(S)
        self.upper_bound = 2 ** 31 - 1

        def dfs(start):
            for end in range(start + 1, self.bound + 1):
                temp = S[start: end]

                if len(temp) > 1 and temp[0] == '0' or int(temp) > self.upper_bound:
                    return

                self.temp_list.append(temp)

                if len(self.temp_list) > 2:
                    if int(self.temp_list[-1]) == int(self.temp_list[-2]) + int(self.temp_list[-3]):
                        if end == self.bound and not self.res:
                            self.res = self.temp_list[:]
                        else:
                            dfs(end)
                    elif int(self.temp_list[-1]) < int(self.temp_list[-2]) + int(self.temp_list[-3]):
                        pass
                    else:
                        self.temp_list.pop()
                        return
                else:
                    dfs(end)

                self.temp_list.pop()

        dfs(0)
        return [int(num) for num in self.res] if self.res else []


sol = Solution()
# s = "123456579"
# s = "11235813"
# s = "112358130"
# s = "1101111"
# s = "0000"
# s = "0123"
# s = "0224"
s = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
print(sol.splitIntoFibonacci(s))
