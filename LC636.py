class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        res = [0] * n
        stack = []
        
        for log in logs:
            idx, act, time = log.split(":")
            idx = int(idx)
            time = int(time)
            
            if act == "end":
                if stack and stack[-1][0] == idx:
                    temp = time - stack[-1][2] - stack[-1][3] + 1
                    res[idx] += temp
                    stack.pop()

                    for log in stack:
                        log[3] += temp
            else:
                stack.append([idx, act, time, 0])
        
        return res


sol = Solution()
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# n = 3
# logs = ["0:start:0", "1:start:2", "2:start:3", "2:end:4", "1:end:6", "0:end:8"]
# n = 1
# logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
# n = 3
# logs = ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]
print(sol.exclusiveTime(n, logs))
