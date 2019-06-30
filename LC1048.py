class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        len_words = len(words)
        words.sort(key=lambda n: len(n))
        ch_counts = [[0] * 26 for _ in range(len_words)]
        base = ord('a')
        preds = {}
        memo = [1] * len_words
        
        for idx, word in enumerate(words):
            for ch in word:
                 ch_counts[idx][ord(ch) - base] += 1
                    
        def is_pred(c1, c2):
            if (c1, c2) in preds:
                return preds[c1, c2]
            
            count = 0
            
            for n1, n2 in zip(ch_counts[c1], ch_counts[c2]):
                if n1 == n2:
                    continue
                else:
                    if n2 - n1 == 1:
                        count += 1
                    else:
                        preds[c1, c2] = False
                        return False
            
            preds[c1, c2] = count == 1
            return preds[c1, c2]
            
        for idx, word in enumerate(words):
            len_word = len(word)

            for pre_idx in range(idx, -1, -1):
                len_pre_word = len(words[pre_idx])
                if len_pre_word == len_word:
                    continue
                elif len_word - len_pre_word == 1:
                    if is_pred(pre_idx, idx):
                        memo[idx] = max(memo[idx], memo[pre_idx] + 1)
                else:
                    break
        
        return max(memo)


sol = Solution()
w = ["heond","wmbhhot","afdzknhh","mdsimgpqewdwoo","wmbhthviot","slepzhpi","pkvhvwdcqsrbt","glkdcip","vnkwnwznjiiebjst","pkvhwdcqsrbt","sdveezfru","krxbxoxhgupawp","hfuoymvwzerk","nqqzqmjbxjg","huomvzrk","zsmqpwc","oiugsmf","oiugsmfrw","vllpohgnj","afgpocwiptcken","zricanuvv","wqdctrivii","nqqjbxjg","beeedij","hyqamuuqbtpayl","zricavjnuvv","afdznkjnthh","joniyugswsmfreww","rxxoxhgpwp","wsijcjazz","vlvlpibohglnj","beei","wtccvloxactpi","wvngcdrmkpm","jatspqmvczxbezt","slepzhpiat","beeedivjh","oniugsmfrew","yaub","hon","hvizwkbeoc","zricavjnuyvv","slepzhpia","wmbhthvot","slxegpzhpiaetd","nswoj","pkwdcqsrbt","ztgocsvgild","swoj","zrmicavjnuymvv","thnufatvyuzsy","slxegpzhpihauetd","hyqaubtpal","krxbxoxhgpwp","slxegpzhpiatd","dh","yqaubt","vlvlpiibonfhglnj","bbeeedivjh","zspwc","wmbhhvot","nqqozvqmjbxjg","jatspqmvczxbz","ztgcsvgl","qtsloluy","ztcsvgl","mdbzvfpceaaebk","aspmvcxbz","t","oiugsmfr","msimgpqedwoo","bpbga","eqtslsoluby","og","n","homvzrk","rwrlqltzsinaxt","dzh","nswojj","yqaub","oigsmf","zpsmqpwc","ogf","kwdcqsrbt","phzboklxxikhwy","bbeeedievdjh","vlvlpibonfhglnj","wbhho","wsijpmchjnazz","hojm","ttpmv","wsijchjazz","riuddyqramdwo","wcloxacp","vllpognj","zpwc","vngcdrmkp","swj","kwcrb","slxegpzhpiauetd","hvizwhkbehoc","krxbxoxhgupwp","aspmcbz","wvungcdrmckpm","jaspqmvczxbz","jatspqmvczxbez","kbexhubrl","heonydea","vlvlpibohgnj","wccloxacp","hfuoymvwzrk","vlvlpbohgnj","lepzpi","mdsximgpqewdwoo","tp","clgqzo","sveezfru","sdvejoezfru","ttp","hyqtamuuqbtpayl","s","hozrk","nqqyozvqmjbxjg","hyqaubtpl","dzhh","hyqaubtp","hho","ttpm","dbzvfpceaaebk","zrmicavjnuyvv","jatspqmvczxbezvt","nnvswojj","ztgcsvgil","beeedijh","wmbhthfviot","ehojm","beeedi","eqtsloluy","vlpgnj","svgl","homzrk","mdbzvflpceaaebk","wccloxacpi","slepzpi","heoojnmydea","ho","nqzqmjbxjg","cgqzo","nqzqjbxjg","oniugssmfrew","wrsiyqzrswvudn","wrsiyzrswvudn","bbeeeedievdjh","e","heoojnydea","zricnuvv","sdvejwoezfru","vngcdrmkpm","aspmvcbz","csvgl","hyqaubt","krxbxoxhgupawwbp","wvungcdrmkpm","dbzvfceaebk","slxegpzhpiat","khyqtamuuqbtpayl","msimgpqewdwoo","zpsmqpawc","pehojm","heon","vnkwnwzjiebjst","wtccvloxaectpi","cb","nqqzvqmjbxjg","glhub","bbseeeedievxdjhc","vlvlpibofhglnj","bbeeeedievxdjh","sw","ezi","joniyugssmfreww","hfuomvwzrk","wbhhot","vlgnj","eriuddyqramduwo","wvqdzctrivikki","bei","jaspmvczxbz","kwcrbt","whho","eqtslsoluy","vllpbohgnj","bpbaga","heondea","hfuoyamvwzerk","slxepzhpiat","joniugssmfrew","glkcip","aspmb","r","wmbhthfvviot","xhnvizwhkbehoc","kwcsrbt","afdznhh","o","zricajnuvv","pkhwdcqsrbt","dbzvfpceaebk","zetgocsvgild","be","aspmbz","yab","fdznhh","oiugsmfrew","svg","hvizwhkbeoc","hoj","joniyugssmfrew","nqzqyozfvqmjbxjg","afdzknthh","heoojnymyodea","sdvejwoezfrju","pkvhvwdcqksrbt","vnkwnwznjiebjst","epzpi","fdzhh","afgpoclwiptcken","ezpi","zcsvgl","nvswojj","hfuomvzrk","ogsmf","wsijpchjazz","kwcqsrbt","wvqdctriviki","bbeeeedievxdjhc","heonda","zsmpwc","beedi","ogmf","ho","heoojnymydea","wtccvloxacpi","jaspmvcxbz","vnkwnwziebjst","wsijcjaz","hyqamubtpayl","nqzqyozvqmjbxjg","hyqamuubtpayl","afdzkjnthh","xhnvizwqhkbehoc","sveezfu","c","ry","wtccloxacpi","krxxoxhgpwp","sdvejezfru","wqdctriviki","on","tmtpmv","peheojm","bbeeedievjh","krxbxoxhgupawbp","riuddyqramduwo","ztgocsvgil","vlpognj","wvqdzctriviki","mimgpqedwoo","wsijpmchjazz","hnvizwhkbehoc","heoonydea","hyqamubtpal","tsloluy","uzrmricavjnuymvv","zrmricavjnuymvv"]
# w = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
print(sol.longestStrChain(w))
