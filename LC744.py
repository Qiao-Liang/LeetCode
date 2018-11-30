class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len_letters = len(letters)

        while left < right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid
            elif letters[mid] < target:
                left = mid + 1
            else:
                left = mid + 1

                while left < right:
                    mid = (left + right) // 2

                    if letters[mid] == target:
                        left = mid + 1
                    else:
                        right = mid

                break

        return letters[left % len_letters]


sol = Solution()
letters = ["c", "f", "j"]
target = "a"

# letters = ["e","e","e","e","e","e","n","n","n","n"]
# target = "e"

print(sol.nextGreatestLetter(letters, target))
        