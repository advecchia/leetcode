# https://leetcode.com/problems/generate-parentheses/

from typing import List
from itertools import permutations
import unittest

MINIMUM_N_VALUE = 1
MAXIMUM_N_VALUE = 8

class SolutionValidator(object):
    def validate_n_value(self, n_value: int) -> None:
        if MINIMUM_N_VALUE > n_value or n_value > MAXIMUM_N_VALUE:
            raise ValueError('Invalid n value')


class Solution:
    def __init__(self):
        """ Given n pairs of parentheses, 
            write a function to generate all combinations of well-formed parentheses.
        """
        self.validator = SolutionValidator()
        self.close_matches = {')':'('}

    def make_combinations(self, n: int) -> List[str]:
        pairs = ''
        for i in range(n):
            pairs += '()'

        # A start list with all parentheses
        parts = list(pairs)
        for combination in permutations(parts, len(parts)):
            yield list(combination)

    def is_valid_parentheses(self, combination: List[str]) -> bool:
        stack = []
        for char in combination:
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

    def generateParenthesis_not_time_efficient(self, n: int) -> List[str]:
        self.validator.validate_n_value(n)
        output = set()
        for combination in self.make_combinations(n):
            if self.is_valid_parentheses(combination):
                output.add(''.join(combination))

        return list(output)

    def generateParenthesis(self, n: int) -> List[str]:
        """ Intuition: To enumerate something, generally we would like to express it as a sum 
            of disjoint subsets that are easier to count.

            Consider the closure number of a valid parentheses sequence S: 
            the least index >= 0 so that S[0], S[1], ..., S[2*index+1] is valid. 
            Clearly, every parentheses sequence has a unique closure number. 
            We can try to enumerate them individually.
            
            Algorithm: For each closure number c, we know the starting and ending brackets 
            must be at index 0 and 2*c + 1. Then, the 2*c elements between must be a valid 
            sequence, plus the rest of the elements must be a valid sequence.
        """
        self.validator.validate_n_value(n)
        return self.generate_parenthesis_recursive(n)

    def generate_parenthesis_recursive(self, n: int) -> List[str]:
        if n == 0:
            return ['']

        output = []
        for closure in range(n):
            for inner_pair in self.generate_parenthesis_recursive(closure):
                for outer_pair in self.generate_parenthesis_recursive(n - 1 - closure):
                    output.append('({}){}'.format(inner_pair, outer_pair))

        return output


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(set(sol.generateParenthesis(3)), set(['((()))','(()())','(())()','()(())','()()()']))

    print('Example 2')
    tc.assertEqual(set(sol.generateParenthesis(1)), set(['()']))


if __name__ == "__main__":
    main()