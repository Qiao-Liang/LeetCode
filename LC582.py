class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        pid_dict = {}

        # Builds the tree
        for p, c in zip(ppid, pid):
            if p in pid_dict:
                pid_dict[p].append(c)
            else:
                pid_dict[p] = [c]

        stack = [kill]
        kill_nodes = []

        while len(stack) > 0:
            count = len(stack)
            while count > 0:
                curr = stack.pop()

                kill_nodes.append(curr)
                if curr in pid_dict:
                    stack.extend(pid_dict[curr])
                count -= 1

        return kill_nodes

# class Solution(object):
#     def killProcess(self, pid, ppid, kill):
#         """
#         :type pid: List[int]
#         :type ppid: List[int]
#         :type kill: int
#         :rtype: List[int]
#         """
#         pid_dict = {}

#         # Builds the tree
#         for p, c in zip(ppid, pid):
#             if p in pid_dict:
#                 pid_dict[p].append(c)
#             else:
#                 pid_dict[p] = [c]

#         stack = [kill]
#         for i in stack:
#             stack.extend(pid_dict.get(i, []))
        
#         return stack

# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]

# sol = Solution()
# kill_nodes = sol.killProcess(pid, ppid, 5)
