class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        if not cpdomains:
            return []

        dic = {}

        for domain in cpdomains:
            count, url = domain.split(" ")
            count = int(count)
            url = url.split(".")
            
            for idx in range(len(url)):
                temp = ".".join(url[idx:])

                if temp in dic:
                    dic[temp] += count
                else:
                    dic[temp] = count

        return ["{0} {1}".format(count, url) for url, count in dic.items()]


sol = Solution()
d = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(sol.subdomainVisits(d))

["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
