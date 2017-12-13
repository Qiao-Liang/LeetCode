class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        stat_dict = {}
        start = ord('a')

        for s in strs:
            temp = [0] * 26

            for c in s:
                temp[ord(c) - start] += 1

            temp = ''.join(map(str, temp))
            if temp in stat_dict:
                stat_dict[temp].append(s)
            else:
                stat_dict[temp] = [s]

        return [stat_dict[key] for key in stat_dict.keys()]

sol = Solution()
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
result = sol.groupAnagrams(strs)
