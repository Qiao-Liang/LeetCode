class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        arr1 = map(int, version1.split('.'))
        arr2 = map(int, version2.split('.'))
        idx = 0
        
        for n1, n2 in zip(arr1, arr2):
            idx += 1

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1

        if len(arr1) > len(arr2):
            return 1 if any([n > 0 for n in arr1[idx:]]) > 0 else 0
        elif len(arr1) < len(arr2):
            return -1 if any([n > 0 for n in arr2[idx:]]) > 0 else 0
        else:
            return 0


sol = Solution()
version1 = "1.0.0"
version2 = "1"
print sol.compareVersion(version1, version2)   
