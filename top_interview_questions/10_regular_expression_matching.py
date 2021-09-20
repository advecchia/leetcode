# https://leetcode.com/problems/regular-expression-matching/
# Solution could be a Finite Automaton with empty transition
# https://en.wikipedia.org/wiki/Kleene%27s_algorithm
import unittest

MINIMUM_WORD_LENGTH = 1
MAXIMUM_WORD_LENGTH = 20
MINIMUM_PATTERN_LENGTH = 1
MAXIMUM_PATTERN_LENGTH = 30

class SolutionValidator(object):
    def validate_word_length(self, word: str):
        if (word is None) or (MINIMUM_WORD_LENGTH > len(word)) or (len(word) > MAXIMUM_WORD_LENGTH):
            raise ValueError('Invalid string length')

    def validate_pattern_length(self, pattern: str):
        if (pattern is None) or (MINIMUM_PATTERN_LENGTH > len(pattern)) or (len(pattern) > MAXIMUM_PATTERN_LENGTH):
            raise ValueError('Invalid pattern length')

    def validate_word_char(self, char: str):
        if not (char.isalpha() and char.islower()):
            raise ValueError('Invalid word character found: ' + char)

    def validate_pattern_char(self, char: str):
        # It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
        if not ((char.isalpha() and char.islower()) or (char in ['.', '*'])):
            raise ValueError('Invalid pattern character found: ' + char)


class Solution:
    """Given an input string s and a pattern p, implement regular expression matching 
    with support for '.' and '*' where:
        '.' Matches any single character.​​​​
        '*' Matches zero or more of the preceding element.
    
    The matching should cover the entire input string (not partial).
    """
    def __init__(self):
        self.validator = SolutionValidator()
        self.cache = {} # tuple based key

    # ---------------------------------------------------------------------------------------------------------
    def isMatch_bottom_up(self, s: str, p: str) -> bool:
        """ Dynamic programming solution - Bottom-up variation
        """
        # TODO: Not working as expected
        # Executes basic validation
        self.validator.validate_word_length(s)
        self.validator.validate_pattern_length(p)

        # Creates a matrix with pairs for string vs pattern
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]

                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

    # ---------------------------------------------------------------------------------------------------------
    def isMatch_top_down(self, s: str, p: str) -> bool:
        # Executes basic validation
        # TODO: Not working as expected
        self.validator.validate_word_length(s)
        self.validator.validate_pattern_length(p)

        return self.dp_match_top_down(s, p, 0, 0)

    def dp_match_top_down(self, s: str, p: str, i: int, j: int) -> bool:
        """ Dynamic programming solution - Top-Down variation
        """
        if (i, j) not in self.cache:
            if j == len(p):
                answer = i == len(s)

            else:
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    answer = self.dp_match_top_down(s, p, i, j + 2) or first_match and self.dp_match_top_down(s, p, i + 1, j)

                else:
                    answer = first_match and self.dp_match_top_down(s, p, i + 1, j + 1)

            self.cache[i, j] = answer
            print('(i,j) = ('+str(i)+', '+str(j)+') = ' + str(answer))

        return self.cache[i, j]

    # ---------------------------------------------------------------------------------------------------------
    def isMatch(self, s: str, p: str) -> bool:
        """ Kleene's algorithm solution
        """
        # Executes basic validation
        self.validator.validate_word_length(s)
        self.validator.validate_pattern_length(p)

        return self.kleene_match(s, p)

    def kleene_match(self, s: str, p: str) -> bool:
        if not p:
            return not s

        first_match = bool(s) and (p[0] in {s[0], '.'})

        if (len(p) >= 2) and (p[1] == '*'):
            return self.kleene_match(s, p[2:]) or first_match and self.kleene_match(s[1:], p)

        else:
            return first_match and self.kleene_match(s[1:], p[1:])


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1:')
    print('Explanation: "a" does not match the entire string "aa".')
    tc.assertEqual(sol.isMatch('aa', 'a'), False)

    print('Example 2:')
    print('Explanation: "*" means zero or more of the preceding element, "a". Therefore, by repeating "a"')
    tc.assertEqual(sol.isMatch('aa', 'a*'), True)

    print('Example 3:')
    print('Explanation: ".*" means "zero or more (*) of any character (.)".')
    tc.assertEqual(sol.isMatch('ab', '.*'), True)

    print('Example 4:')
    print('Explanation: "c" can be repeated 0 times, "a" can be repeated 1 time. Therefore, it matches "aab".')
    tc.assertEqual(sol.isMatch('aab', 'c*a*b'), True)

    print('Example 5:')
    tc.assertEqual(sol.isMatch('mississippi', 'mis*is*p*.'), False)

    print('Example 6:')
    tc.assertEqual(sol.isMatch('abcxxccddd', 'abc..ccd*'), True)

    print('Example 7:')
    tc.assertEqual(sol.isMatch('abx', 'abc*.*pp'), False)

    print('Example 8:')
    tc.assertEqual(sol.isMatch('abpp', 'abc*.*pp'), True)


if __name__ == "__main__":
    main()