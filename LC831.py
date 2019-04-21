class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if S[0].isalpha():
            name, domain = S.split('@')
            return '{}*****{}@{}'.format(name[0], name[-1], domain).lower()
        else:
            digits = [ch for ch in S if ch.isdigit()]
            res = "***-***-{}".format(digits[-4:])

            if len(digits) > 10:
                return "+{}-{}".format("*" * (len(digits) - 10), res)

        # if S[0].isalpha():
        #     name, domain = S.split('@')
        #     return ''.join([name[0].lower(), "*" * 5, name[-1].lower(), "@", domain.lower()])
        # else:
        #     digits = [ch for ch in S if ch.isdigit()]
        #     res = '-'.join(["*" * 3, "*" * 3, ''.join(digits[-4:])])
            
        #     if len(digits) > 10:
        #         return ''.join(["+" , "*" * (len(digits) - 10), '-']) + res
        #     else:
        #         return res


sol = Solution()
print(sol.maskPII("86-(10)12345678"))
