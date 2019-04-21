from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para_len = len(paragraph)
        ban_set = set(banned)
        counter = Counter()
        idx = 0

        while idx < para_len:
            if paragraph[idx].isalpha():
                end_idx = idx + 1

                while end_idx < para_len and paragraph[end_idx].isalpha():
                    end_idx += 1

                word = paragraph[idx: end_idx].lower()

                if word not in ban_set:
                    counter[word] += 1
            
                idx = end_idx
            else:
                idx += 1

        return counter.most_common(1)[0][0]


sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph, banned))
