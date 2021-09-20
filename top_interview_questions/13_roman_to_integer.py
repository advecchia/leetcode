import unittest

MINIMUM_WORD_LENGTH = 1
MAXIMUM_WORD_LENGTH = 15

class SolutionValidator(object):
    def validate_word_length(self, word: str) -> None:
        if MINIMUM_WORD_LENGTH > len(word) or len(word) > MAXIMUM_WORD_LENGTH:
            raise ValueError('Invalid word length')

    def validate_roman_char(self, char: str) -> None:
        if char not in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            raise ValueError('Invalid Roman char')


class Solution:
    def __init__(self):
        self.validator = SolutionValidator()
        self.roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        # Basic validations
        self.validator.validate_word_length(s)

        total = 0
        last = -2**32
        for i in range(len(s) - 1, -1, -1):
            # Basic validations
            self.validator.validate_roman_char(s[i])

            current = self.roman_map[s[i]]
            if last > current:
                total -= current

            else:
                total += current

            last = current

        return total

def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(sol.romanToInt('III'), 3)

    print('Example 2')
    tc.assertEqual(sol.romanToInt('IV'), 4)

    print('Example 3')
    tc.assertEqual(sol.romanToInt('IX'), 9)

    print('Example 4')
    print('Explanation: L = 50, V= 5, III = 3.')
    tc.assertEqual(sol.romanToInt('LVIII'), 58)

    print('Example 5')
    print('Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.')
    tc.assertEqual(sol.romanToInt('MCMXCIV'), 1994)


if __name__ == "__main__":
    main()