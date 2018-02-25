class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sen_list = sentence.split(' ')
        
        for idx, word in enumerate(sen_list):
            min_root = word
            len_word = len(word)

            for root in dict:
                len_root = len(root)

                if  len_root < len(min_root) and len_root <= len_word and word[:len_root] == root:
                    min_root = root

            sen_list[idx] = min_root

        return ' '.join(sen_list)


sol = Solution()
# dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
dict = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(sol.replaceWords(dict, sentence))
