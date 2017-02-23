"""
Palindrome Partitioning
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s or s == "":
            return []
        
        self.result = []
        self.recurse(s, [])
        
        return self.result
    
    def recurse(self, s, solution):
        """
        s: the string to be checked
        solution: a possible partition of palindromes
        result: the collection of all solutions
        """
        if len(s) == 0:
            self.result.append(solution[:])
            return
        
        for i in range(len(s)):
            temp = s[:i + 1]

            if temp == temp[::-1]:
                solution.append(temp)

                self.recurse(s[i + 1:], solution)
                solution.pop()  # Backtracking
