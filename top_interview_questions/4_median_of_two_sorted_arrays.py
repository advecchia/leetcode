# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List
import unittest

MINIMUM_ARRAY_LENGTH = 0
MAXIMUM_ARRAY_LENGTH = 10**3
MINIMUM_ARRAY_LENGTH_M_N = 1
MAXIMUM_ARRAY_LENGTH_M_N = 2 * MAXIMUM_ARRAY_LENGTH
MINIMUM_ARRAY_VALUE = -10**6
MAXIMUM_ARRAY_VALUE = 10**6

class SolutionValidator(object):
    def validate_array_length(self, array: List[int]) -> None:
        if MINIMUM_ARRAY_LENGTH > len(array) > MAXIMUM_ARRAY_LENGTH:
            raise ValueError('Invalid array length')

    def validate_array_m_n_length(self, array_m: List[int], array_n: List[int]) -> None:
        if MINIMUM_ARRAY_LENGTH_M_N > len(array_m) + len(array_n) > MAXIMUM_ARRAY_LENGTH_M_N:
            raise ValueError('Invalid array m + arry n length')

    def validate_array_value(self, value: int) -> None:
        if MINIMUM_ARRAY_VALUE > value > MAXIMUM_ARRAY_VALUE:
            raise ValueError('Invalid array value')


class Solution:
    def __init__(self):
        self.validator = SolutionValidator()

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:        
        # Basic validations
        self.validator.validate_array_length(nums1)
        self.validator.validate_array_length(nums2)
        self.validator.validate_array_m_n_length(nums1, nums2)

        median = 0
        total_array_length = len(nums1) + len(nums2)
        if total_array_length > 0:
            # The overall run time complexity should be O(log (m+n)).
            full_array = self.array_merge(nums1, nums2)
            # odd length
            median = full_array[total_array_length//2]
            if (total_array_length % 2) == 0:
                # pair length
                median = (full_array[(total_array_length//2) - 1] + median) / 2
 
        return median

    def array_merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        full_array = []
        full_array.extend(nums1)
        full_array.extend(nums2)
        full_array.sort()

        return full_array


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1: nums1 = [1,3], nums2 = [2]')
    print('Explanation: merged array = [1,2,3] and median is 2.')
    tc.assertEqual(sol.findMedianSortedArrays([1,3], [2]), 2.00000)

    print('Example 2: nums1 = [1,2], nums2 = [3,4]')
    print('Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.')
    tc.assertEqual(sol.findMedianSortedArrays([1,2], [3,4]), 2.50000)

    print('Example 3: nums1 = [0,0], nums2 = [0,0]')
    tc.assertEqual(sol.findMedianSortedArrays([0,0], [0,0]), 0.00000)

    print('Example 4: nums1 = [], nums2 = [1]')
    tc.assertEqual(sol.findMedianSortedArrays([], [1]), 1.00000)

    print('Example 5: nums1 = [2], nums2 = []')
    tc.assertEqual(sol.findMedianSortedArrays([2], []), 2.00000)

    print('Example 6: nums1 = [1,3], nums2 = [2,7]')
    tc.assertEqual(sol.findMedianSortedArrays([1,3], [2,7]), 2.50000)

    print('Example 7: nums1 = [0,9,34,120], nums2 = [4,5,6,7,11,25,700]')
    tc.assertEqual(sol.findMedianSortedArrays([0,9,34,120], [4,5,6,7,11,25,700]), 9.00000)

if __name__ == "__main__":
    main()