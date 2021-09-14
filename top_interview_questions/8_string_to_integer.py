# https://leetcode.com/problems/string-to-integer-atoi/
import unittest

MINIMUM_INT_VALUE = -2**31
MAXIMUM_INT_VALUE = 2**31 -1
# MINIMUM_WORD_LENGTH = 0 # But we can ignore the validation
MAXIMUM_WORD_LENGTH = 200

class SolutionValidator(object):
    def validate_word_length(self, word: str) -> None:
        if (word is None) or (len(word) > MAXIMUM_INT_VALUE):
            raise ValueError('Invalid string length')

    def is_valid_char(self, char: str) -> bool:
        if char.isdecimal() or (char in ['+', '-']):
            return True

        return False

    def return_correct_value(self, value: int) -> int:
        if MINIMUM_INT_VALUE > value:
            return MINIMUM_INT_VALUE

        if value > MAXIMUM_INT_VALUE:
            return MAXIMUM_INT_VALUE

        return value


class Solution:
    """ Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
    
    The algorithm for myAtoi(string s) is as follows:
        1. Read in and ignore any leading whitespace.
        2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
        3. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
        4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
        5. If the integer is out of the 32-bit signed integer range [-2**31, (2**31) - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2**31 should be clamped to -2**31, and integers greater than (2**31) - 1 should be clamped to (2**31) - 1.
        6. Return the integer as the final result.

    Note:
        Only the space character ' ' is considered a whitespace character.
        Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
    """
    def __init__(self):
        self.validator = SolutionValidator()

    def myAtoi(self, s: str) -> int:
        # Basic validations
        self.validator.validate_word_length(s)

        sign = ''
        already_signed = False
        read_number = False
        number = ''
        for i in range(len(s)):
            # Ignore empty string
            if s[i] == ' ':
                if already_signed or read_number:
                    break
                continue

            # Breaks for a non numeric string
            if not self.validator.is_valid_char(s[i]):
                break

            if s[i] == '-':
                if already_signed or read_number:
                    break
                else:
                    sign = '-'
                    already_signed = True

            elif s[i] == '+':
                if already_signed or read_number:
                    break
                else:
                    already_signed = True

            else:
                number += s[i]
                read_number = True

        # Clean up starting zeroes
        number = number.lstrip('0')
        if len(number) == 0:
            return 0

        # Merge number string using the sign, convert to int and validate limits
        return self.validator.return_correct_value(int(sign + number))


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1:')
    tc.assertEqual(sol.myAtoi('42'), 42)

    print('Example 2:')
    tc.assertEqual(sol.myAtoi('   -42'), -42)

    print('Example 3:')
    tc.assertEqual(sol.myAtoi('4193 with words'), 4193)

    print('Example 4:')
    tc.assertEqual(sol.myAtoi('words and 987'), 0)

    print('Example 5:')
    tc.assertEqual(sol.myAtoi('-91283472332'), -2147483648)

    print('Example 6:')
    tc.assertEqual(sol.myAtoi('1-2'), 1)

    print('Example 7:')
    tc.assertEqual(sol.myAtoi('-9+222'), -9)

    print('Example 8:')
    tc.assertEqual(sol.myAtoi('4 6'), 4)

    print('Example 9:')
    tc.assertEqual(sol.myAtoi('  +  413'), 0)


if __name__ == "__main__":
    main()