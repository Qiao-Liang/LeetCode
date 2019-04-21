class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def count(s):
            temp = []
            bound = len(s)
            idx = 0

            while idx < bound:
                count = 1
                temp_idx = idx

                while temp_idx + 1 < bound and s[temp_idx] == s[temp_idx + 1]:
                    count += 1
                    temp_idx += 1

                temp.append((s[idx], count))
                idx += count
            
            return temp

        temp_s = count(S)
        res = 0
        len_s = len(temp_s)

        for word in words:
            temp_word = count(word)

            if len(temp_word) == len_s:
                to_add = 1

                for s, w in zip(temp_s, temp_word):
                    if s[0] == w[0] and (s[1] == w[1] == 2 or s[1] == w[1] == 1 or (s[1] >= 3 and s[1] >= w[1])):
                        continue
                    else:
                        to_add = 0
                        break
                
                res += to_add

        return res


sol = Solution()
# S = "heeellooo"
# words = ["hello", "hi", "helo"]

# S = "zzzzzyyyyy"
# words = ["zzyy","zy","zyy"]

# S = "dddiiiinnssssssoooo"
# words = ["dinnssoo","ddinso","ddiinnso","ddiinnssoo","ddiinso","dinsoo","ddiinsso","dinssoo","dinso"]

S = "ggkyyyyffffbbhddddrxxsiixccqqqqkmmmiiiiiivvvyyuuujccuuuhhhhwssssnnttoyuuuussggttttfeeeebbbbeedddddqq"
words = ["ggkyyfbbhdrxxsiixccqkmmiiivvvyyujccuuuhhwsnnttoyuuussggtttfeeebbbeedddqq","ggkyyfffbbhddrxxsiixccqqkmmmiiiivvvyyuujccuuuhhhwsnnttoyuuussggtttfebeedddddqq","ggkyyyyffbbhdrxxsiixccqkmmiiiivyyujccuhhwsssnnttoyuuussggtfebeeddddqq","ggkyyfffbbhdddrxxsiixccqkmmmiiiiivyyujccuuhhwsssnnttoyuuussggtfebbeeddddqq","ggkyyyyfffbbhdddrxxsiixccqkmmmiiivvvyyuujccuhhwssnnttoyuuussggtfeeebbbeedddddqq","ggkyyyyfffbbhddrxxsiixccqqkmiiiiivyyuuujccuuuhwsnnttoyuussggtfeebbbeedddddqq","ggkyyffbbhdddrxxsiixccqqkmiiiiivvyyuujccuhwsnnttoyussggtttfeeebbbeedddqq","ggkyyyfbbhddrxxsiixccqqqkmiiivvvyyuuujccuhhwsnnttoyuussggttfebeeddddqq","ggkyyyfbbhdrxxsiixccqqqkmmiiiivvyyujccuuhwsnnttoyussggtfeebbeedddqq","ggkyyyfbbhdddrxxsiixccqkmmmiiiivyyuujccuhhhwsssnnttoyuussggttfeeebeedddqq","ggkyyyfbbhdrxxsiixccqkmmiiiiivyyujccuhhhwssnnttoyussggtttfeebeedddqq","ggkyyyfffbbhddrxxsiixccqqqkmmmiiivvyyuuujccuuhhhwssnnttoyuussggttfeebeedddddqq","ggkyyfffbbhdrxxsiixccqqkmmiiiiivvyyuuujccuuuhhwsnnttoyuussggttfeebbeedddddqq","ggkyyfffbbhdddrxxsiixccqkmiiiivyyuuujccuuhwssnnttoyuussggtfebeedddddqq","ggkyyyyfffbbhddrxxsiixccqqkmmiiivyyuujccuuuhhwssnnttoyussggtfebbbeedddddqq","ggkyyyyffbbhdrxxsiixccqkmmiiiivyyujccuhwsssnnttoyussggtttfebeeddddqq","ggkyyyfbbhddrxxsiixccqqkmiiiiivvyyuuujccuhhhwsssnnttoyuuussggttfeeebbbeedddqq","ggkyyyyffbbhdddrxxsiixccqkmmmiiiivvvyyuuujccuuhhhwssnnttoyussggtttfeeebbbeeddddqq","ggkyyyfbbhdddrxxsiixccqqqkmiiivvvyyuujccuuhhwsnnttoyuuussggtfeebbbeedddqq","ggkyyyffbbhdddrxxsiixccqqqkmiiiivvyyuuujccuuhwssnnttoyuussggttfeebbbeedddqq","ggkyyyyfbbhdddrxxsiixccqkmmmiiiiivvvyyujccuuhhwsnnttoyuuussggttfebbbeedddddqq","ggkyyyfbbhdddrxxsiixccqqqkmmiiiivvyyuujccuuhhwssnnttoyuuussggttfebeeddddqq","ggkyyyyfbbhddrxxsiixccqkmmiiivvvyyuujccuuhhhwsnnttoyussggtfeeebbbeedddqq","ggkyyyfffbbhdrxxsiixccqqkmiiiiivvyyujccuuhwsnnttoyussggtttfeebbeedddddqq","ggkyyyyfffbbhddrxxsiixccqqqkmiiiivyyuuujccuuuhhwsssnnttoyuuussggttfebbeedddqq","ggkyyffbbhddrxxsiixccqkmiiivvyyujccuuhwssnnttoyuuussggtttfeebbeedddddqq","ggkyyyfffbbhdddrxxsiixccqqkmmmiiiiivvyyuuujccuuuhhwssnnttoyussggtttfeeebbeeddddqq","ggkyyyyfbbhddrxxsiixccqkmmmiiivvvyyujccuuhhhwssnnttoyuuussggtfeeebbeedddddqq","ggkyyyyfffbbhdddrxxsiixccqkmmmiiiivyyuuujccuhhhwsssnnttoyuussggtttfeeebbeedddddqq","ggkyyyyfbbhdrxxsiixccqqkmmiiiiivyyuujccuuuhhwsnnttoyuussggttfebbeedddqq","ggkyyyfbbhdrxxsiixccqkmiiiivvyyujccuhhhwsnnttoyussggttfeeebbeedddddqq","ggkyyyfffbbhddrxxsiixccqqqkmiiivyyuujccuuuhhwssnnttoyuuussggtfeebeedddqq","ggkyyffbbhdrxxsiixccqqkmmiiiiivyyuujccuhhhwsnnttoyuuussggtfebeedddddqq","ggkyyyfffbbhddrxxsiixccqkmiiiiivvvyyuujccuuuhhwsnnttoyuuussggttfeeebbeeddddqq","ggkyyyfffbbhdddrxxsiixccqqkmmmiiiivvyyuujccuuhwssnnttoyuussggtfebeedddqq","ggkyyfbbhdddrxxsiixccqqkmiiiiivyyujccuuuhhwsssnnttoyuuussggtttfeeebeeddddqq","ggkyyyyffbbhdddrxxsiixccqqkmmiiiiivvyyuuujccuuhhhwssnnttoyuussggtfeebbbeedddddqq","ggkyyffbbhdrxxsiixccqkmmiiiivyyuujccuuhhhwssnnttoyuussggtfeebeeddddqq","ggkyyyffbbhddrxxsiixccqkmmiiiiivvyyujccuuuhhwssnnttoyuussggtttfeeebbbeeddddqq","ggkyyyfffbbhdrxxsiixccqqqkmiiiivvvyyuujccuhhhwsssnnttoyuuussggtttfebbeeddddqq","ggkyyffbbhdrxxsiixccqqkmiiiiivyyuuujccuuuhwsnnttoyuuussggttfeeebbeeddddqq","ggkyyyfbbhdrxxsiixccqqkmiiivyyujccuuuhhhwsnnttoyussggtfebbbeeddddqq","ggkyyfffbbhddrxxsiixccqqkmmiiivyyuujccuuuhhwsnnttoyuussggtttfeeebbeedddddqq","ggkyyyyfbbhdrxxsiixccqqkmmmiiiiivvvyyujccuuuhhhwssnnttoyuussggtttfeebbeeddddqq","ggkyyyffbbhdrxxsiixccqqqkmiiiivvvyyuuujccuuhhhwsssnnttoyussggtttfeebeeddddqq","ggkyyyyfbbhddrxxsiixccqkmiiiiivvvyyuuujccuuuhhwssnnttoyuussggttfeeebeeddddqq","ggkyyyyffbbhdrxxsiixccqqkmmiiivvvyyuujccuuhhhwsnnttoyuussggttfeeebbbeedddqq","ggkyyfffbbhddrxxsiixccqkmiiiiivvyyuuujccuuuhwsssnnttoyuuussggtttfebeedddddqq","ggkyyyfbbhdrxxsiixccqkmmmiiiiivvyyuuujccuuuhwssnnttoyuussggttfeeebbeedddddqq","ggkyyyffbbhdrxxsiixccqkmmiiiivyyujccuuuhhwssnnttoyussggtttfebbbeeddddqq","ggkyyyffbbhdrxxsiixccqqkmmmiiiivvvyyuujccuhwssnnttoyussggtfebeeddddqq","ggkyyyffbbhdddrxxsiixccqqkmiiivvyyuujccuuhhhwssnnttoyussggtfeebbeeddddqq","ggkyyyffbbhdrxxsiixccqqqkmmiiiivvvyyujccuhhhwsnnttoyuuussggttfebbbeedddqq","ggkyyyfbbhddrxxsiixccqqkmiiiiivvyyuujccuuhhwsssnnttoyuuussggtfebbbeeddddqq","ggkyyffbbhddrxxsiixccqqkmmiiiiivvyyujccuhhhwsssnnttoyuuussggtttfeebbbeedddddqq","ggkyyyfffbbhdrxxsiixccqqkmiiivvyyuujccuhhwsssnnttoyuussggttfeeebbeedddqq","ggkyyyfffbbhdrxxsiixccqkmmmiiiivvyyuujccuuuhwssnnttoyussggtfebbbeeddddqq","ggkyyyyffbbhdrxxsiixccqqkmiiiivvvyyuuujccuuhwsnnttoyuussggttfebbbeedddddqq","ggkyyyyffbbhddrxxsiixccqqkmmmiiiiivvyyuuujccuhwsssnnttoyuussggtfeeebbeeddddqq","ggkyyyyfbbhdddrxxsiixccqqkmmiiivyyujccuuuhhwsssnnttoyussggtfebbeedddqq","ggkyyyffbbhdrxxsiixccqkmiiiiivvyyuujccuhhwssnnttoyussggtfebeedddqq","ggkyyyffbbhdrxxsiixccqkmmiiivyyujccuuhhhwsssnnttoyuuussggtttfeeebbbeeddddqq","ggkyyyyfffbbhdddrxxsiixccqqqkmmmiiiiivvyyujccuuhhhwssnnttoyuuussggtttfebbbeedddqq","ggkyyyfbbhdddrxxsiixccqqkmmiiivvvyyujccuuuhhhwssnnttoyuussggtttfebbbeeddddqq","ggkyyyfbbhdrxxsiixccqqqkmmmiiivvyyuuujccuuhhwsssnnttoyuuussggtttfebeedddqq","ggkyyyyfbbhddrxxsiixccqkmmiiiiivvvyyuuujccuuhhwssnnttoyuuussggtfeeebeedddddqq","ggkyyyyfffbbhdddrxxsiixccqqkmiiiivvyyujccuuhhwsssnnttoyussggtfebbbeedddqq","ggkyyyffbbhdrxxsiixccqqkmmmiiivvyyuuujccuhhhwsssnnttoyussggtttfebbbeeddddqq","ggkyyyfffbbhdddrxxsiixccqqkmmmiiiiivvvyyuuujccuuuhhwsnnttoyuussggttfeebeedddddqq","ggkyyyyfffbbhdddrxxsiixccqqqkmmmiiiivvyyuuujccuuuhhhwsssnnttoyussggtfeebbbeedddddqq","ggkyyyfbbhdddrxxsiixccqkmiiiiivyyuuujccuhhhwsnnttoyuussggtttfeebeedddqq","ggkyyyfbbhdrxxsiixccqqqkmmmiiiiivyyujccuhhwsnnttoyuussggttfeebbeedddqq","ggkyyyyffbbhdrxxsiixccqqqkmmiiivvyyujccuhhhwssnnttoyussggttfeeebbbeedddddqq","ggkyyyfffbbhdrxxsiixccqqqkmiiiiivyyujccuhhwsssnnttoyuuussggtfeebbbeeddddqq","ggkyyyffbbhdrxxsiixccqqkmiiiivvyyuuujccuhhhwssnnttoyussggttfeeebbbeedddqq","ggkyyyyffbbhdrxxsiixccqkmiiiiivvyyuujccuhhwssnnttoyuussggtfeeebeedddqq","ggkyyyfbbhdddrxxsiixccqkmmmiiivvyyujccuuhhhwsssnnttoyuussggtttfeebeedddddqq","ggkyyyyfffbbhdddrxxsiixccqqqkmmmiiiiivvvyyuuujccuuhwssnnttoyuuussggtfeeebbeedddddqq","ggkyyfbbhdrxxsiixccqkmiiiivvyyujccuuuhhhwssnnttoyuussggttfebbeedddqq","ggkyyyfbbhddrxxsiixccqqqkmmiiiivyyuujccuuhhwsnnttoyuussggttfebbeedddddqq","ggkyyyyfbbhdddrxxsiixccqkmmiiivyyujccuhwsssnnttoyussggttfeebbbeedddqq","ggkyyyyfbbhdrxxsiixccqkmiiiiivvvyyuuujccuuuhhwsnnttoyuuussggtfeebeeddddqq","ggkyyffbbhddrxxsiixccqqkmmiiiivyyuujccuuhhwsssnnttoyuussggtttfeeebbeedddqq","ggkyyyfffbbhddrxxsiixccqqqkmmiiivvvyyuujccuhhwsnnttoyuussggttfebbbeeddddqq","ggkyyfffbbhdrxxsiixccqkmmmiiivvvyyuuujccuuuhwsssnnttoyussggttfeeebeedddddqq","ggkyyyyffbbhdrxxsiixccqqqkmmiiiiivvyyuuujccuhhwsnnttoyuuussggtttfeeebbeedddqq","ggkyyyyfffbbhdrxxsiixccqkmmiiivvvyyuujccuhhwsssnnttoyuuussggttfeebbeedddddqq","ggkyyyyfffbbhdddrxxsiixccqqqkmiiivvyyuuujccuuhhhwssnnttoyuuussggttfebbbeedddddqq","ggkyyffbbhdrxxsiixccqqqkmmmiiiiivvvyyujccuuuhwsssnnttoyuussggtttfeeebbbeeddddqq","ggkyyyyfffbbhdddrxxsiixccqkmmmiiiiivyyujccuuuhwsnnttoyuuussggtttfeeebeedddddqq","ggkyyfffbbhdrxxsiixccqkmmmiiiiivvyyuujccuuuhwsssnnttoyussggtfebbeedddddqq","ggkyyyyfbbhddrxxsiixccqqqkmiiivyyuujccuuhhhwssnnttoyussggttfeeebbbeedddddqq","ggkyyffbbhddrxxsiixccqkmmiiivvvyyuuujccuuhhwsssnnttoyuuussggtfeeebbeedddddqq","ggkyyffbbhdddrxxsiixccqkmiiiivvvyyuujccuuhhhwsssnnttoyuuussggttfebbeedddqq","ggkyyyyffbbhdrxxsiixccqkmmmiiiiivyyuujccuuuhwsnnttoyuuussggtttfebeeddddqq","ggkyyffbbhddrxxsiixccqkmmmiiiivyyuuujccuuhhhwsssnnttoyuuussggtfeeebeedddqq","ggkyyyyfbbhdrxxsiixccqkmmmiiivyyuujccuhwsnnttoyuuussggtttfeeebbeeddddqq","ggkyyyyfffbbhdddrxxsiixccqqkmiiivvyyuujccuhhhwsnnttoyuuussggttfeeebbeedddqq","ggkyyyyfffbbhdddrxxsiixccqqkmmmiiivvyyuuujccuuuhwssnnttoyuussggtttfeebeedddqq","ggkyyyyfffbbhdddrxxsiixccqkmiiiiivyyuujccuuuhhwssnnttoyussggtttfeeebeeddddqq"]

print(sol.expressiveWords(S, words))
