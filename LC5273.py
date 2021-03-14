class Solution:
    def suggestedProducts(self, products, searchWord: str):
        words = products
        curr = ''
        l = 0
        res = []
        
        for c in searchWord:
            temp = []
            curr += c
            l += 1
            
            for w in words:
                if w[:l] == curr:
                    temp.append(w)
                    
            temp.sort()
            res.append(temp[:3])
            words = temp
            
        return res


sol = Solution()
p = [["mobile","mouse","moneypot","monitor","mousepad"], "mouse"]
print(sol.suggestedProducts(*p))
