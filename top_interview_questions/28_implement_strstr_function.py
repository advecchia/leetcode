# https://leetcode.com/problems/implement-strstr/

import unittest

MAXIMUM_INPUT_LENGTH = 5 * 10**4

class SolutionValidator(object):
    def validate_input_length(self, input_len: int) -> None:
        if input_len > MAXIMUM_INPUT_LENGTH:
            raise ValueError('Invalid input string length')

    def validate_islower(self, string: str) -> None:
        if not string.islower():
            raise ValueError('Invalid input string case')

class Solution:
    def __init__(self):
        """ Implement strStr(). http://www.cplusplus.com/reference/cstring/strstr/
            Return the index of the first occurrence of needle in haystack, 
            or -1 if needle is not part of haystack.

            Clarification:
            What should we return when needle is an empty string? 
            This is a great question to ask during an interview.

            For the purpose of this problem, we will return 0 when needle is an empty string. 
            This is consistent to C's strstr() and Java's indexOf().
        """
        self.validator = SolutionValidator()

    def strStr(self, haystack: str, needle: str) -> int:
        # Basic validation on haystack
        haystack_len = len(haystack)
        self.validator.validate_input_length(haystack_len)

        # Basic validation on needle
        needle_len = len(needle)
        self.validator.validate_input_length(needle_len)

        found = -1
        if needle_len > haystack_len:
            return found

        elif needle == haystack:
            return 0

        # Case validation on both haystack and needle
        if haystack_len > 0:
            self.validator.validate_islower(haystack)

        if needle_len > 0:
            self.validator.validate_islower(needle)

        for increment in range(haystack_len - needle_len + 1):
            if haystack[increment:needle_len + increment] == needle:
                return increment

        return found


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(sol.strStr('hello', 'll'), 2)

    print('Example 2')
    tc.assertEqual(sol.strStr('aaaaa', 'bba'), -1)

    print('Example 3')
    tc.assertEqual(sol.strStr('', ''), 0)

    print('Example 4')
    tc.assertEqual(sol.strStr('abc', 'abcd'), -1)

    print('Example 5')
    tc.assertEqual(sol.strStr('a', ''), 0)

    print('Example 6')
    tc.assertEqual(sol.strStr('abc', 'c'), 2)

    print('Example 7')
    tc.assertEqual(sol.strStr('', 'c'), -1)

if __name__ == "__main__":
    main()