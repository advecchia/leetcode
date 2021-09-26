# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List
import unittest

MINIMUM_DIGIT_VALUE = 2
#MAXIMUM_DIGIT_VALUE = 9 # no need to verify
# MINIMUM_DIGIT_LENGTH = 0 # no need to verify
MAXIMUM_DIGIT_LENGTH = 4
PHONE_MAPPING = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}

class SolutionValidator(object):
    def validate_digit_value(self, digit: str) -> None:
        digit_value = None
        try:
            digit_value = int(digit)

        except Exception:
            # Digit is not a number
            raise ValueError('Invalid number value')

        if MINIMUM_DIGIT_VALUE > digit_value:
            raise ValueError('Invalid number value')

    def validate_digit_length(self, digit_len: int) -> None:
        if digit_len > MAXIMUM_DIGIT_LENGTH:
            raise ValueError('Invalid array length')


class Solution:
    def __init__(self):
        """ Given a string containing digits from 2-9 inclusive, 
            return all possible letter combinations that the number could represent. 
            Return the answer in any order.

            A mapping of digit to letters (just like on the telephone buttons) is given below. 
            Note that 1 does not map to any letters.
        """
        self.validator = SolutionValidator()

    def merge_letters(self, ar1: List[str], ar2: List[str]) -> List[str]:
        return [x+y for x in ar1 for y in ar2]

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        len_digits = len(digits)
        self.validator.validate_digit_length(len_digits)

        letters = []
        for i in range(len_digits):
            self.validator.validate_digit_value(digits[i])
            letters.append(PHONE_MAPPING[digits[i]])

        len_letters = len(letters)
        if len_letters == 1:
            return letters[0]

        elif len_letters == 2:
            return self.merge_letters(letters[0], letters[1])

        elif len_letters == 3:
            partial_01 = self.merge_letters(letters[0], letters[1])
            return self.merge_letters(partial_01, letters[2])

        else:
            partial_01 = self.merge_letters(letters[0], letters[1])
            partial_23 = self.merge_letters(letters[2], letters[3])
            return self.merge_letters(partial_01, partial_23)


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(sol.letterCombinations('23'), ['ad','ae','af','bd','be','bf','cd','ce','cf'])

    print('Example 2')
    tc.assertEqual(sol.letterCombinations(''), [])

    print('Example 3')
    tc.assertEqual(sol.letterCombinations('2'), ['a','b','c'])

    print('Example 4')
    tc.assertEqual(sol.letterCombinations('234'), ['adg','adh','adi','aeg','aeh','aei','afg','afh','afi','bdg','bdh','bdi','beg','beh','bei','bfg','bfh','bfi','cdg','cdh','cdi','ceg','ceh','cei','cfg','cfh','cfi'])


if __name__ == "__main__":
    main()