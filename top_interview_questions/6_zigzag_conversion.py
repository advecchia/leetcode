# https://leetcode.com/problems/zigzag-conversion/
import unittest

MINIMUM_WORD_LENGTH = 1
MAXIMUM_WORD_LENGTH = 10**3
MINIMUM_ROWS_LENGTH = 1
MAXIMUM_ROWS_LENGTH = 10**3

class SolutionValidator(object):
    def validate_word_length(self, word: str) -> None:
        if word is None or MINIMUM_WORD_LENGTH > len(word) > MAXIMUM_WORD_LENGTH:
            raise ValueError('Invalid string length')

    def validate_num_rows_size(self, num_rows: int) -> None:
        if num_rows is None or MINIMUM_ROWS_LENGTH > num_rows > MAXIMUM_ROWS_LENGTH:
            raise ValueError('Invalid numRows value')

    def validate_word_char(self, char: str) -> None:
        if not (char.isalpha() or char in ['.', ',']):
            raise ValueError('Invalid char in string')


class Solution:
    def __init__(self):
        self.validator = SolutionValidator()

    def convert(self, s: str, numRows: int) -> str:
        # Basic validations
        self.validator.validate_word_length(s)
        self.validator.validate_num_rows_size(numRows)

        if numRows == 1:
            # Validates each char before return
            [self.validator.validate_word_char(char) for char in list(s)]
            # Simple case where string will keep the same as the input
            return s

        output = dict()
        pos = 0
        descending = True
        for i in range(len(s)):
            # Validates each char
            self.validator.validate_word_char(s[i])

            try:
                output[pos] += s[i]

            except KeyError:
                output[pos] = s[i]

            if (pos < numRows - 1) and descending:
                pos += 1

            else:
                pos -= 1
                descending = False

                if pos < 1:
                    descending = True

        return ''.join([substring for substring in output.values()])


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1:')
    tc.assertEqual(sol.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')

    print('Example 2:')
    tc.assertEqual(sol.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')

    print('Example 3:')
    print('Explanation: \nP     I    N\nA   L S  I G\nY A   H R\nP     I')
    tc.assertEqual(sol.convert('A', 1), 'A')

    print('Example 4:')
    tc.assertEqual(sol.convert(',', 1), ',')

    print('Example 5:')
    tc.assertEqual(sol.convert('.', 1), '.')

    print('Example 6:')
    tc.assertEqual(sol.convert('ABC', 1), 'ABC')

    print('Example 6:')
    tc.assertEqual(sol.convert('ABC', 2), 'ACB')

if __name__ == "__main__":
    main()