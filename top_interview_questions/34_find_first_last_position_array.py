# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List
import unittest

MINIMUM_ARRAY_LENGTH = 0
MAXIMUM_ARRAY_LENGTH = 10**5
MINIMUM_NUMBER_VALUE = -10**9
MAXIMUM_NUMBER_VALUE = 10**9

class SolutionValidator(object):
    def validate_array_length(self, array_len: int) -> None:
        if MINIMUM_ARRAY_LENGTH > array_len or array_len > MAXIMUM_ARRAY_LENGTH:
            raise ValueError('Invalid array length')

    def validate_number_value(self, number: int) -> None:
        if MINIMUM_NUMBER_VALUE > number or number > MAXIMUM_NUMBER_VALUE:
            raise ValueError('Invalid number value')


class Solution:
    def __init__(self):
        """ Given an array of integers nums sorted in ascending order, 
            find the starting and ending position of a given target value.

            If target is not found in the array, return [-1, -1].
            You must write an algorithm with O(log n) runtime complexity.
        """
        self.validator = SolutionValidator()

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Basic validations
        len_nums = len(nums)
        self.validator.validate_array_length(len_nums)
        self.validator.validate_number_value(target)

        # Target not in array
        start_pos = -1
        end_pos = -1
        if not nums:
            return [start_pos, end_pos]

        # Search for a start pivot, then use three strategies
        pivot = len_nums//2
        if nums[pivot] == target:
            # Look around
            left = pivot
            right = pivot
            while left >= 0 and nums[left] == target:
                self.validator.validate_number_value(nums[left])
                left -= 1
            start_pos = left + 1
            while right < len_nums and nums[right] == target:
                self.validator.validate_number_value(nums[right])
                right += 1
            end_pos = right - 1

        elif nums[pivot] < target:
            # go right
            start = pivot
            while start < len_nums and nums[start] != target:
                self.validator.validate_number_value(nums[start])
                start += 1
            if start < len_nums:
                start_pos = start
                end_pos = start
                while end_pos < len_nums and nums[end_pos] == target:
                    self.validator.validate_number_value(nums[end_pos])
                    end_pos += 1
                end_pos -= 1
        else:
            # go left
            end = pivot
            while end >= 0 and nums[end] != target:
                self.validator.validate_number_value(nums[end])
                end -= 1
            if end >= 0:
                start_pos = end
                end_pos = end
                while start_pos >= 0 and nums[start_pos] == target:
                    self.validator.validate_number_value(nums[start_pos])
                    start_pos -= 1
                start_pos += 1

        return [start_pos, end_pos]


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(sol.searchRange([5,7,7,8,8,10], 8), [3,4])

    print('Example 2')
    tc.assertEqual(sol.searchRange([5,7,7,8,8,10], 6), [-1,-1])

    print('Example 3')
    tc.assertEqual(sol.searchRange([], 0), [-1,-1])

    print('Example 4')
    tc.assertEqual(sol.searchRange([9], 0), [-1,-1])

    print('Example 5')
    tc.assertEqual(sol.searchRange([0,1,2,3,4,5,6,7,8,9,10,94,94,94,94,94,95,96,97,98,99], 94), [11,15])

    print('Example 6')
    tc.assertEqual(sol.searchRange([7,7,7,7,7,7,7,7,7,7,7], 7), [0,10])

    print('Example 7')
    tc.assertEqual(sol.searchRange([1,2,3,4,5,6,7,8,9,19], 19), [9,9])

    print('Example 8')
    tc.assertEqual(sol.searchRange([1,2,3,4,5,6,7,8,9,19], 1), [0,0])

if __name__ == "__main__":
    main()