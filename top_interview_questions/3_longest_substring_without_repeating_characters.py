import unittest

MINIMUM_STR_LENGTH = 0
MAXIMUM_STR_LENGTH = 5 * 10**4

class SolutionValidator(object):
    def validate_string_length(self, word: str) -> None:
        if (not word.isprintable()) or (MINIMUM_STR_LENGTH > len(word) > MAXIMUM_STR_LENGTH):
            raise ValueError('Invalid string length')


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        validator = SolutionValidator()
        validator.validate_string_length(s)

        # break word in chars
        word = [c for c in s]
        longest_substring = 0
        temp = []
        cont = 0
        while(cont < len(s)):
            for i in range(cont, len(s)):
                if word[i] in temp:
                    break

                temp.append(word[i])


            if longest_substring < len(temp):
                longest_substring = len(temp)
            temp = []
            cont += 1

        return longest_substring


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1: The answer is "abc", with the length of 3.')
    tc.assertEqual(sol.lengthOfLongestSubstring('abcabcbb'), 3)

    print('Example 2: The answer is "b", with the length of 1.')
    tc.assertEqual(sol.lengthOfLongestSubstring('bbbbb'), 1)

    print('Example 3: The answer is "wke", with the length of 3.')
    print('Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.')
    tc.assertEqual(sol.lengthOfLongestSubstring('pwwkew'), 3)

    print('Example 4')
    tc.assertEqual(sol.lengthOfLongestSubstring(''), 0)

    print('Example 5')
    tc.assertEqual(sol.lengthOfLongestSubstring('abba'), 2)

if __name__ == "__main__":
    main()