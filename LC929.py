class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        dic = {}

        for email in emails:
            name, domain = email.split('@')
            name = name.split('+')[0].replace('.','')

            if domain in dic:
                dic[domain].add(name)
            else:
                dic[domain] = set([name])

        return sum([len(val) for key, val in dic.items()])


sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(sol.numUniqueEmails(emails))
        