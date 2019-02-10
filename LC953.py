class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        dic = [0] * 26
        base = ord('a')

        for idx, ch in enumerate(order):
            dic[ord(ch) - base] = idx

        for idx in range(1, len(words)):
            left = words[idx - 1]
            right = words[idx]
            len_left = len(left)
            len_right = len(right)
            left_idx = right_idx = 0

            while left_idx < len_left and right_idx < len_right:
                if dic[ord(left[left_idx]) - base] < dic[ord(right[right_idx]) - base]:
                    break
                elif dic[ord(left[left_idx]) - base] > dic[ord(right[right_idx]) - base]:
                    return False
                else:
                    left_idx += 1
                    right_idx += 1

            if right_idx == len_right and left[left_idx - 1] == right[right_idx - 1] and len_left > len_right:
                return False

        return True


sol = Solution()
# words = ["hello","leetcode"]
words = ["hello","l"]
order = "hlabcdefgijkmnopqrstuvwxyz"
# words = ["word","world","row"]
# order = "worldabcefghijkmnpqstuvxyz"
# words = ["apple","app"]
# order = "abcdefghijklmnopqrstuvwxyz"
# words = ["ubg","kwh"]
# order = "qcipyamwvdjtesbghlorufnkzx"
print(sol.isAlienSorted(words, order))
        