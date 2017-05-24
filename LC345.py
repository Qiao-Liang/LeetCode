class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = list(s)
        head = 0
        tail = len(temp) - 1
        vowels = 'aeiouAEIOU'
        
        while head <= tail:
            if not temp[head] in vowels:
                head += 1
            elif not temp[tail] in vowels:
                tail -= 1
            else:
                temp[head], temp[tail] = temp[tail], temp[head]
                
                head += 1
                tail -= 1
        
        return ''.join(temp)
        