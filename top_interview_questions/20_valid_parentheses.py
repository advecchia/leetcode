# https://leetcode.com/problems/valid-parentheses/

import unittest

MINIMUM_STRING_LENGTH = 1
MAXIMUM_STRING_LENGTH = 10**4
VALID_CHARS = ['(',')','[',']','{','}']

class SolutionValidator(object):
    def validate_string_length(self, str_len: int) -> None:
        if MINIMUM_STRING_LENGTH > str_len or str_len > MAXIMUM_STRING_LENGTH:
            raise ValueError('Invalid string length')

    def validate_chars(self, char: str) -> None:
        if char not in VALID_CHARS:
            raise ValueError('Invalid char value')

class Solution:
    def __init__(self):
        """ Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
        determine if the input string is valid.

            An input string is valid if:
                - Open brackets must be closed by the same type of brackets.
                - Open brackets must be closed in the correct order.
        """
        self.validator = SolutionValidator()
        self.close_matches = {')':'(', ']':'[', '}':'{'}

    def isValid(self, s: str) -> bool:
        # Basic validations
        self.validator.validate_string_length(len(s))

        stack = []
        for char in list(s):
            self.validator.validate_chars(char)
            if stack:
                top = stack.pop()
                if char not in self.close_matches or top != self.close_matches[char]:
                    stack.append(top)
                    stack.append(char)

            else:
                stack.append(char)

        if stack:
            return False

        return True


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(sol.isValid('()'), True)

    print('Example 2')
    tc.assertEqual(sol.isValid('()[]{}'), True)

    print('Example 3')
    tc.assertEqual(sol.isValid('(]'), False)

    print('Example 4')
    tc.assertEqual(sol.isValid('([)]'), False)

    print('Example 5')
    tc.assertEqual(sol.isValid('{[]}'), True)

    print('Example 6')
    tc.assertEqual(sol.isValid('({{}[()()()]{}})'), True)

    print('Example 7')
    tc.assertEqual(sol.isValid('(){}}{'), False)


if __name__ == "__main__":
    main()