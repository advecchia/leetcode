# https://leetcode.com/problems/reverse-integer/
import unittest

MINIMUM_INT_VALUE = -2**31
MAXIMUM_INT_VALUE = (2**31) -1

class SolutionValidator(object):
    def validate_int_value(self, value: int) -> None:
        if (value is None) or (MINIMUM_INT_VALUE > value) or (value > MAXIMUM_INT_VALUE):
            raise ValueError('Invalid string length')

    def validate_reversed_int_value(self, value: int) -> None:
        if (MINIMUM_INT_VALUE > value) or (value > MAXIMUM_INT_VALUE):
            return 0
        else:
            return value


class Solution:
    def __init__(self):
        self.validator = SolutionValidator()

    def reverse(self, x: int) -> int:
        # Basic validations
        self.validator.validate_int_value(x)

        if x == 0:
            return x

        output = 1
        if x < 0:
            x *= -1
            output = -1

        numbers = list(str(x))
        numbers.reverse()
        output *= int(''.join(numbers).rstrip().lstrip('0'))

        return self.validator.validate_reversed_int_value(output)


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1:')
    tc.assertEqual(sol.reverse(123), 321)

    print('Example 2:')
    tc.assertEqual(sol.reverse(-123), -321)

    print('Example 3:')
    tc.assertEqual(sol.reverse(120), 21)

    print('Example 4:')
    tc.assertEqual(sol.reverse(0), 0)

    print('Example 5:')
    tc.assertEqual(sol.reverse(-0), 0)

    print('Example 6:')
    tc.assertEqual(sol.reverse(- 123120000), -21321)

    print('Example 7:')
    tc.assertRaises(ValueError, sol.reverse, 340282366920938463463374607431768211456)

    print('Example 8:')
    tc.assertRaises(ValueError, sol.reverse, None)

    print('Example 9:')
    tc.assertEqual(sol.reverse(1534236469), 0)

if __name__ == "__main__":
    main()