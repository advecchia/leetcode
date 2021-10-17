# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List
import unittest

MINIMUM_ARRAY_LENGTH = 1
MAXIMUM_ARRAY_LENGTH = 5 * 10**3
MINIMUM_NUMBER_VALUE = -10**4
MAXIMUM_NUMBER_VALUE = 10**4

class SolutionValidator(object):
    def validate_array_length(self, array_len: int) -> None:
        if MINIMUM_ARRAY_LENGTH > array_len or array_len > MAXIMUM_ARRAY_LENGTH:
            raise ValueError('Invalid array length')

    def validate_number_value(self, number: int) -> None:
        if MINIMUM_NUMBER_VALUE > number or number > MAXIMUM_NUMBER_VALUE:
            raise ValueError('Invalid number value')

    def validate_unique_numbers(self, len_array: int, len_set: int) -> None:
        if len_array != len_set:
            raise ValueError('The array numbers are not unique')


class Solution:
    def __init__(self):
        """ There is an integer array nums sorted in ascending order (with distinct values).

            Prior to being passed to your function, nums is possibly rotated at an unknown 
            pivot index k (1 <= k < nums.length) such that the resulting array is 
            [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
            For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

            Given the array nums after the possible rotation and an integer target, return the index 
            of target if it is in nums, or -1 if it is not in nums.

            You must write an algorithm with O(log n) runtime complexity.
        """
        self.validator = SolutionValidator()

    def search(self, nums: List[int], target: int) -> int:
        # Basic validations
        len_nums = len(nums)
        self.validator.validate_array_length(len_nums)
        self.validator.validate_unique_numbers(len_nums, len(set(nums)))
        self.validator.validate_number_value(target)

        result = -1 # target not in array
        end = len_nums -1
        for start in range(len_nums//2 + 1):
            self.validator.validate_number_value(nums[start])
            if nums[start] == target:
                return start

            self.validator.validate_number_value(nums[end - start])
            if nums[end - start] == target:
                return end - start

        return result


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(sol.search([4,5,6,7,0,1,2], 0), 4)

    print('Example 2')
    tc.assertEqual(sol.search([4,5,6,7,0,1,2], 3), -1)

    print('Example 3')
    tc.assertEqual(sol.search([1], 0), -1)

    print('Example 4')
    tc.assertEqual(sol.search([9], 0), -1)

    print('Example 5')
    tc.assertEqual(sol.search([94,95,96,97,98,99,0,1,2,3,4,5,6,7,8,9,10], 5), 11)

if __name__ == "__main__":
    main()