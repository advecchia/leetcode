# https://leetcode.com/problems/container-with-most-water/
from typing import List
import unittest

MINIMUM_HEIGHT_LENGTH = 2
MAXIMUM_HEIGHT_LENGTH = 10**5
MINIMUM_HEIGHT_VALUE = 0
MAXIMUM_HEIGHT_VALUE = 10**4

class SolutionValidator(object):
    def validate_height_length(self, height: List[int]):
        if (height is None) or (MINIMUM_HEIGHT_LENGTH > len(height)) or (len(height) > MAXIMUM_HEIGHT_LENGTH):
            raise ValueError('Invalid height length')

    def validate_height_value(self, value: int):
        if (value is None) or (MINIMUM_HEIGHT_VALUE > value) or (value > MAXIMUM_HEIGHT_VALUE):
            raise ValueError('Invalid height value')


class Solution:
    def __init__(self):
        self.validator = SolutionValidator()

    def maxArea(self, height: List[int]) -> int:
        # Executes basic validation
        self.validator.validate_height_length(height)

        # Validate values:
        for h in height:
            self.validator.validate_height_value(h)

        max_capacity = -1
        left = 0
        right = len(height) - 1
        while(left < right):
            # Leet code solution: one pass O(n) points to barrier positions and move from
            # border parts to center moving the pointer from lesser value. Stop when they
            # cross each other.
            max_capacity = max(max_capacity, min(height[left], height[right])*(right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_capacity

    def maxArea_not_time_efficient_3(self, height: List[int]) -> int:
        # Executes basic validation
        self.validator.validate_height_length(height)

        # Validate values:
        for h in height:
            self.validator.validate_height_value(h)

        # Make a list of valid pairs to exexcute calculations
        capacities = [ (end-start)*min(height[start], height[end]) for start in range(len(height)) for end in range(len(height)) if start != end and start < end ]

        return max(capacities)

    def maxArea_not_memory_efficient_2(self, height: List[int]) -> int:
        # Executes basic validation
        self.validator.validate_height_length(height)

        # Validate values:
        for h in height:
            self.validator.validate_height_value(h)

        # Make a list of valid pairs to exexcute calculations
        pairs = [ (start, end) for start in range(len(height)) for end in range(len(height)) if start != end and start < end ]

        # Loop the array, compare two values, 
        # use the small to calculate the water container between those two values
        # keep that number until another greater value shows.
        max_capacity = -1
        for i, j in pairs:
            distance = j - i
            limit = min(height[i], height[j])

            capacity = limit * distance
            if capacity > max_capacity:
                max_capacity = capacity

        return max_capacity

    def maxArea_not_time_efficient_1(self, height: List[int]) -> int:
        # Executes basic validation
        self.validator.validate_height_length(height)

        # Loop the array, compare two values, 
        # use the small to calculate the water container between those two values
        # keep that number until another greater value shows.
        max_capacity = -1
        for i in range(len(height)):
            self.validator.validate_height_value(height[i])
            for j in range(i + 1, len(height)):
                self.validator.validate_height_value(height[j])

                distance = j - i
                limit = min(height[i], height[j])

                capacity = limit * distance
                if capacity > max_capacity:
                    max_capacity = capacity

        return max_capacity


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1:')
    print('Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.')
    tc.assertEqual(sol.maxArea([1,8,6,2,5,4,8,3,7]), 49)

    print('Example 2:')
    tc.assertEqual(sol.maxArea([1,1]), 1)

    print('Example 3:')
    tc.assertEqual(sol.maxArea([4,3,2,1,4]), 16)

    print('Example 4:')
    tc.assertEqual(sol.maxArea([1,2,1]), 2)


if __name__ == "__main__":
    main()