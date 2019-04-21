class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        graph = {key: [] for key in A}
        len_a = len(A)

        for left in A:
            for right in A:
                if left != right:
                    l_idx = len(left) - 1
                    r_idx = 0
                    len_r = len(right)
                    overlap = 0

                    while l_idx > -1 and r_idx < len_r:
                        if left[l_idx:] == right[:r_idx + 1]:
                            overlap = r_idx + 1

                        l_idx -= 1
                        r_idx += 1

                    graph[left].append((right, overlap))

        self.max_overlap = 0
        self.res = None

        def dfs(key, visited, path, overlap):
            if len(visited) == len_a:
                if overlap > self.max_overlap:
                    self.max_overlap = overlap
                    self.res = path[:]
            else:
                for next_key, next_overlap in graph[key]:
                    if next_key not in visited:
                        visited.add(next_key)
                        dfs(next_key, visited, path + [(next_key, next_overlap)], overlap + next_overlap)
                        visited.remove(next_key)


        for key in graph:
            graph[key].sort(key=lambda n: n[1])
            dfs(key, set([key]), [(key, 0)], 0)

        return ''.join([key[idx:] for key, idx in self.res]) if self.res else ''.join(A)


sol = Solution()
a = ["catg","ctaagt","gcta","ttca","atgcatc"]
# a = ["isirisjwbauawjku","kbptmisirisjwbauawj","misirisjwbauawjk","uiwcuysnxuyzevfzdbwd","ddenazwremyzyuyxw","zwremyzyuyxwstx","zdbwdeoepihbddenaz","zskkbptmisirisjwbaua","epihbddenazwremyzyuy"]
print(sol.shortestSuperstring(a))
