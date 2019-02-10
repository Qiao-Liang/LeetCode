class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if not IP:
            return "Neither"
        elif '.' in IP:
            nums = IP.split('.')

            if len(nums) != 4:
                return "Neither"
            
            for num in nums:
                if not num or (len(num) > 1 and num[0] == '0') or not num.isdigit() or not (0 <= int(num) <= 255):
                    return "Neither"

            return "IPv4"
        elif ':' in IP:
            nums = IP.split(':')
            cands = "0123456789abcdefABCDEF"

            if len(nums) != 8:
                return "Neither"

            for num in nums:
                if len(num) == 0 or len(num) > 4:
                    return "Neither"

                for d in num:
                    if d not in cands:
                        return "Neither"

            return "IPv6"
        else:
            return "Neither"


sol = Solution()
# IP = "172.16.254.1"
# IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
# IP = "256.256.256.256"
# IP = "2001:0db8:85a3::8A2E:0370:7334"
IP = "192.0.0.1"
print(sol.validIPAddress(IP))
        