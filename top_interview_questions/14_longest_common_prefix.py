# https://leetcode.com/problems/longest-common-prefix/

from typing import List
import unittest

MINIMUM_WORD_LENGTH = 0
MAXIMUM_WORD_LENGTH = 200
MINIMUM_ARRAY_LENGTH = 1
MAXIMUM_ARRAY_LENGTH = 200

class SolutionValidator(object):
    def validate_word_length(self, word: str) -> None:
        if len(word) == MINIMUM_WORD_LENGTH:
            return

        if (not (word.isalpha() and word.islower())) or len(word) > MAXIMUM_WORD_LENGTH:
            raise ValueError('Invalid word')

    def validate_array_length(self, array_len: int) -> None:
        if MINIMUM_ARRAY_LENGTH > array_len or array_len > MAXIMUM_ARRAY_LENGTH:
            raise ValueError('Invalid array length')


class Solution:
    def __init__(self):
        self.validator = SolutionValidator()

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Basic validations
        len_array = len(strs)
        self.validator.validate_array_length(len_array)

        if len_array == 1:
            self.validator.validate_word_length(strs[0])
            return strs[0]

        lcp = ''
        try:
            for i in range(MAXIMUM_WORD_LENGTH):
                current_lcp = ''
                start = 0
                end = len_array - 1
                while start <= end:
                    self.validator.validate_word_length(strs[start])
                    self.validator.validate_word_length(strs[end])
                    if strs[start][i] != strs[end][i]:
                        raise ValueError

                    if not current_lcp:
                        current_lcp = strs[start][i]

                    elif strs[start][i] != current_lcp:
                        raise ValueError
                    
                    start += 1
                    end -= 1

                lcp += current_lcp

        except IndexError:
            pass

        except ValueError:
            pass

        return lcp


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(sol.longestCommonPrefix(['flower','flow','flight']), 'fl')

    print('Example 2')
    tc.assertEqual(sol.longestCommonPrefix(['dog','racecar','car']), '')

    print('Example 3')
    tc.assertEqual(sol.longestCommonPrefix(['dog']), 'dog')

    print('Example 4')
    tc.assertEqual(sol.longestCommonPrefix(['doga','dogb','dogc','racecar','dogd','doge','dogf',]), '')

    print('Example 5')
    tc.assertEqual(sol.longestCommonPrefix(['dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog','dogdogdogdogdogdogdogdogdogdog']), 'dogdogdogdogdogdogdogdogdogdog')

    print('Example 6')
    tc.assertEqual(sol.longestCommonPrefix(['']), '')

    print('Example 7')
    tc.assertEqual(sol.longestCommonPrefix(['', '', '', '', '', '', '', '', '']), '')


if __name__ == "__main__":
    main()