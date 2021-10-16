# https://leetcode.com/problems/divide-two-integers/

import unittest

MINIMUM_NUMBER_VALUE = -2**31
MAXIMUM_NUMBER_VALUE = 2**31 - 1
MAXIMUM_POWER_NUMBER = 31

class SolutionValidator(object):
    def validate_number_value(self, number: int) -> None:
        if MINIMUM_NUMBER_VALUE > number or number > MAXIMUM_NUMBER_VALUE:
            raise ValueError('Invalid number value')

    def validate_divisor(self, divisor: int) -> None:
        if divisor == 0:
            raise ValueError('Invalid divisor value, zero')

    def is_overflow(self, result: int) -> int:
        if MINIMUM_NUMBER_VALUE > result or result > MAXIMUM_NUMBER_VALUE:
            return MAXIMUM_NUMBER_VALUE

        return result


class Solution:
    def __init__(self):
        """ Given two integers dividend and divisor, divide two integers without 
            using multiplication, division, and mod operator.

            Return the quotient after dividing dividend by divisor.

            The integer division should truncate toward zero, which means losing 
            its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

            Note: Assume we are dealing with an environment that could only store 
            integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. 
            For this problem, assume that your function returns 2^31 − 1 when the division result overflows.
        """
        self.validator = SolutionValidator()

    def divide(self, dividend: int, divisor: int) -> int:
        # Basic validations
        self.validator.validate_divisor(divisor)
        self.validator.validate_number_value(dividend)
        self.validator.validate_number_value(divisor)

        # Use bitwise operator exclusive or to deal with sign
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        temp_dividend = abs(dividend)
        temp_divisor = abs(divisor)

        quotient = 0
        temp = 0
        for i in range(MAXIMUM_POWER_NUMBER, -1, -1):
            if (temp + (temp_divisor << i) <= temp_dividend):
                temp += temp_divisor << i
                quotient |= 1 << i

        if sign < 0:
            quotient = - quotient

        return self.validator.is_overflow(quotient)

    def divide_not_efficient(self, dividend: int, divisor: int) -> int:
        # Basic validations
        self.validator.validate_divisor(divisor)
        self.validator.validate_number_value(dividend)
        self.validator.validate_number_value(divisor)

        quotient = 0
        remainder = dividend if dividend >= 0 else -dividend
        temp_divisor = divisor if divisor >= 0 else -divisor
        while remainder >= 0:
            remainder -= temp_divisor
            quotient += 1

        quotient -= 1
        if divisor < 0:
            quotient = - quotient

        if dividend < 0:
            quotient = - quotient

        return self.validator.is_overflow(quotient)


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    print('Explanation: 10/3 = truncate(3.33333..) = 3.')
    tc.assertEqual(sol.divide(10, 3), 3)

    print('Example 2')
    print('Explanation: 7/-3 = truncate(-2.33333..) = -2.')
    tc.assertEqual(sol.divide(7, -3), -2)

    print('Example 3')
    tc.assertEqual(sol.divide(0, 1), 0)

    print('Example 4')
    tc.assertEqual(sol.divide(1, 1), 1)

    print('Example 5')
    tc.assertEqual(sol.divide(2, 5), 0)

    print('Example 6')
    tc.assertEqual(sol.divide(-1, -5), 0)

    print('Example 7')
    tc.assertEqual(sol.divide(100, 8), 12)

    print('Example 8')
    tc.assertEqual(sol.divide(-1, 1), -1)

    print('Example 9')
    tc.assertEqual(sol.divide(-2147483648, -1), MAXIMUM_NUMBER_VALUE)

if __name__ == "__main__":
    main()