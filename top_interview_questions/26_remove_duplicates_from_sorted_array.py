# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List
import unittest

MAXIMUM_ARRAY_LENGTH = 3 * 10**4
MINIMUM_NUMBER_VALUE = -100
MAXIMUM_NUMBER_VALUE = 100

class SolutionValidator(object):
    def validate_array_length(self, array_length: int) -> None:
        if array_length > MAXIMUM_ARRAY_LENGTH:
            raise ValueError('Invalid array length')

    def validate_number_value(self, number: int) -> None:
        if MINIMUM_NUMBER_VALUE > number or number > MAXIMUM_NUMBER_VALUE:
            raise ValueError('Invalid number value')


class Solution:
    def __init__(self):
        """ Given an integer array nums sorted in non-decreasing order, 
            remove the duplicates in-place such that each unique element appears only once. 
            The relative order of the elements should be kept the same.

            Since it is impossible to change the length of the array in some languages, 
            you must instead have the result be placed in the first part of the array nums. 
            More formally, if there are k elements after removing the duplicates, then the 
            first k elements of nums should hold the final result. 
            It does not matter what you leave beyond the first k elements.

            Return k after placing the final result in the first k slots of nums.

            Do not allocate extra space for another array. You must do this by modifying 
            the input array in-place with O(1) extra memory.
        """
        self.validator = SolutionValidator()

    def removeDuplicates(self, nums: List[int]) -> int:
        len_nums = len(nums)
        self.validator.validate_array_length(len_nums)
        current = None
        i = 0
        last = len_nums - 1 # Position of the last element
        while i <= last:
            step = nums[i]
            if current != step:
                current = step
                self.validator.validate_number_value(step)
                i += 1

            else:
                del nums[i]
                last -= 1

        return len(nums)


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1') # It does not matter what you leave beyond the returned k (hence they are underscores)
    print('Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.')
    nums = [1,1,2]
    result = sol.removeDuplicates(nums)
    tc.assertEqual(result, 2)
    tc.assertEqual(nums, [1,2])

    print('Example 2') # It does not matter what you leave beyond the returned k (hence they are underscores)
    print('Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.')
    nums = [0,0,1,1,1,2,2,3,3,4]
    result = sol.removeDuplicates(nums)
    tc.assertEqual(result, 5)
    tc.assertEqual(nums, [0,1,2,3,4])

    print('Example 3') # It does not matter what you leave beyond the returned k (hence they are underscores)
    print('Explanation: Your function should return k = 0, with empty elements in nums array.')
    nums = []
    result = sol.removeDuplicates(nums)
    tc.assertEqual(result, 0)
    tc.assertEqual(nums, [])

    print('Example 4') # It does not matter what you leave beyond the returned k (hence they are underscores)
    print('Explanation: Your function should return k = 1, with the first element of nums being 1.')
    nums = [1,1]
    result = sol.removeDuplicates(nums)
    tc.assertEqual(result, 1)
    tc.assertEqual(nums, [1])

    print('Example 5') # It does not matter what you leave beyond the returned k (hence they are underscores)
    print('Explanation: Your function should return k = 2, with the first two elements of nums being 0 and 1 respectively.')
    nums = [0,0,0,0,0,0,0,0,0,1]
    result = sol.removeDuplicates(nums)
    tc.assertEqual(result, 2)
    tc.assertEqual(nums, [0,1])

    print('Example 6') # It does not matter what you leave beyond the returned k (hence they are underscores)
    print('Explanation: Your function should return k = 2, with the first two elements of nums being 0 and 1 respectively.')
    nums = [0,1,1,1,1,1,1,1,1,1,1,1,1,1]
    result = sol.removeDuplicates(nums)
    tc.assertEqual(result, 2)
    tc.assertEqual(nums, [0,1])

if __name__ == "__main__":
    main()