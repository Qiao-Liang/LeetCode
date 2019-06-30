class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        last_idx = {ch: idx for idx, ch in enumerate(text)}
        stack = []
        visited = set([])
            
        for idx, ch in enumerate(text):
            if ch not in visited:
                while stack and stack[-1] > ch and idx < last_idx[stack[-1]]:
                    visited.remove(stack[-1])
                    stack.pop()

                stack.append(ch)
                visited.add(ch)
        
        return ''.join(stack)


sol = Solution()
t = 'cdadabcc'
# t = 'ecbacba'
# t = "cbaacabcaaccaacababa"
print(sol.smallestSubsequence(t))
