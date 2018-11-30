class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        
        if '0000' in deadends:
            return -1

        visited = set([])
        queue = ['0000']
        cand = '0123456789'
        base = ord('0')
        res = 0

        while queue:
            temp_queue = []
            res += 1

            for node in queue:
                for idx in range(4):
                    temp_node = list(node)
                    temp_idx = ord(temp_node[idx]) - base
                    temp_prev_ch, temp_next_ch = cand[(temp_idx + 9) % 10], cand[(temp_idx + 1) % 10]

                    temp_node[idx] = temp_prev_ch
                    temp_prev = ''.join(temp_node)
                    temp_node[idx] = temp_next_ch
                    temp_next = ''.join(temp_node)

                    if temp_prev == target or temp_next == target:
                        return res

                    if temp_prev not in visited and temp_prev not in deadends:
                        temp_queue.append(temp_prev)
                        visited.add(temp_prev)
                    
                    if temp_next not in visited and temp_next not in deadends:
                        temp_queue.append(temp_next)
                        visited.add(temp_next)
            
            queue = temp_queue

        return -1


sol = Solution()
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
# deadends = ["8888"]
# target = "0009"
# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
# target = "8888"
deadends = ["0000"]
target = "8888"

print(sol.openLock(deadends, target))
        