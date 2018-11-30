class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return []

        self.res = []

        def recurse(s, idx, group, temp):
            if group == 3:
                last_group = s[idx:]

                if last_group != '' and not (len(last_group) > 1 and last_group[0] == "0") and int(last_group) < 256:
                    self.res.append('.'.join(temp + [last_group]))
            else:    
                if idx < len(s) and s[idx] == "0":
                    recurse(s, idx + 1, group + 1, temp + ["0"])
                else:
                    end = idx + 1

                    while end < len(s) and int(s[idx: end]) < 256:
                        recurse(s, end, group + 1, temp + [s[idx: end]])
                        end += 1

        recurse(s, 0, 0, [])

        return self.res


sol = Solution()
print sol.restoreIpAddresses("1111")
