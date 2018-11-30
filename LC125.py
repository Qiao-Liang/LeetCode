class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        dic = '0123456789abcdefghijklmnopqrstuvwxyz'

        while right > left:
            temp_left = s[left].lower()

            if temp_left not in dic:
                left += 1
                continue

            temp_right = s[right].lower()

            if temp_right not in dic:
                right -= 1
                continue

            if temp_left == temp_right:
                left += 1
                right -= 1
            else:
                return False

        return True


sol = Solution()
# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = '0p'
print sol.isPalindrome(s)
