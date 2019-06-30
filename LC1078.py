class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        pattern = first + ' ' + second
        idx = 0
        len_text = len(text)
        len_ptrn = len(pattern)
        
        while idx < len_text:
            if text[idx: idx + len_ptrn] == pattern:
                idx += len_ptrn + 1
                temp_idx = idx
                
                while temp_idx < len_text and text[temp_idx] != ' ':
                    temp_idx += 1
                
                if text[idx: temp_idx]:
                    res.append(text[idx: temp_idx])
            else:
                idx += 1
        
        return res

# params = ["we will we will rock you"
# ,"we"
# ,"will"]

params = [
    "ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk"
    ,"lnlqhmaohv"
    ,"ypkk"
]
sol = Solution()
print(sol.findOcurrences(*params))
        