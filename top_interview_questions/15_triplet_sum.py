# https://leetcode.com/problems/3sum/

from typing import List
import unittest

MINIMUM_NUMBER_VALUE = -10**5
MAXIMUM_NUMBER_VALUE = 10**5
MINIMUM_ARRAY_LENGTH = 0
MAXIMUM_ARRAY_LENGTH = 3000

class SolutionValidator(object):
    def validate_number_value(self, number: int) -> None:
        if MINIMUM_NUMBER_VALUE > number or number > MAXIMUM_NUMBER_VALUE:
            raise ValueError('Invalid number value')

    def validate_array_length(self, array_len: int) -> None:
        if MINIMUM_ARRAY_LENGTH > array_len or array_len > MAXIMUM_ARRAY_LENGTH:
            raise ValueError('Invalid array length')


class Solution:
    def __init__(self):
        """ Given an integer array nums, 
            return all the triplets [nums[i], nums[j], nums[k]] 
            such that i != j, i != k, and j != k, 
            and nums[i] + nums[j] + nums[k] == 0.

            Notice that the solution set must not contain duplicate triplets.
        """
        self.validator = SolutionValidator()

    def mygen(self, nums: List[int], len_nums: int):
        for i in range(len_nums-2):
            for j in range(1,len_nums-1):
                if (i != j and i<j):
                    for k in range(2,len_nums):
                        if (i != k and j != k and j<k) and (nums[i] + nums[j] + nums[k]) == 0:
                            yield [i,j,k]

    def threeSum_not_time_efficient(self, nums: List[int]) -> List[List[int]]:
        """ O(n^3)
        """
        # Basic validations
        nums.sort()
        len_nums = len(nums)
        self.validator.validate_array_length(len_nums)

        triplets = dict()
        if len_nums < 3:
            return []

        for i in range(len_nums):
            self.validator.validate_number_value(nums[i])

        for i,j,k in self.mygen(nums, len_nums):
            triplets[str(nums[i])+'#'+str(nums[j])+'#'+str(nums[k])] = [nums[i], nums[j], nums[k]]

        return list(triplets.values())

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ Run in O(n^2)
            Uses a two point technique to traverse the array and use a fixed start value (for iteration) to make the sum.
        """
        # Basic validations
        nums.sort()
        len_nums = len(nums)
        self.validator.validate_array_length(len_nums)

        triplets = dict()
        if len_nums < 3:
            return []

        for i in range(len_nums):
            self.validator.validate_number_value(nums[i])

        for i in range(len_nums-2):
            j = i + 1
            k = len_nums - 1
            while j < k:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    triplets[str(nums[i])+'#'+str(nums[j])+'#'+str(nums[k])] = [nums[i], nums[j], nums[k]]
                    j += 1

                elif (nums[i] + nums[j] + nums[k]) < 0:
                    j += 1

                else:
                    k -= 1

        return list(triplets.values())


def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(sol.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])

    print('Example 2')
    tc.assertEqual(sol.threeSum([]), [])

    print('Example 3')
    tc.assertEqual(sol.threeSum([0]), [])

    print('Example 4')
    tc.assertEqual(sol.threeSum([0,2,1,-2,1,6,-4,3,7,-3,-1]), [[-4,-3,7],[-4,-2,6],[-4,1,3],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-2,1,1],[-1,0,1]])

    print('Example 5')
    tc.assertEqual(sol.threeSum([14,-11,-2,-3,4,-3,-3,-8,-15,11,11,-6,-14,-13,5,-10,-13,0,-12,-8,14,-12,-10,2,-4,9,13,10,2,7,-2,-7,4,11,5,-7,-15,10,-7,-14,6,11,-5,7,6,8,5,8,-7,8,-15,14,11,13,1,-15,7,0,10,-14,14,-15,-14,3,4,6,4,4,-7,12,5,14,0,8,7,13,1,-11,-2,9,12,-1,8,0,-11,-5,0,11,2,-13,4,1,-12,5,-10,-1,-12,9,-12,-11,-2,9,-12,5,-6,2,4,10,6,-13,4,3,-7,-11,11,-3,-9,-4,-15,8,-9,-4,-13,-14,8,14]), [[-15, 1, 14], [-15, 2, 13], [-15, 3, 12], [-15, 4, 11], [-15, 5, 10], [-15, 6, 9], [-15, 7, 8], [-14, 0, 14], [-14, 1, 13], [-14, 2, 12], [-14, 3, 11], [-14, 4, 10], [-14, 5, 9], [-14, 6, 8], [-14, 7, 7], [-13, -1, 14], [-13, 0, 13], [-13, 1, 12], [-13, 2, 11], [-13, 3, 10], [-13, 4, 9], [-13, 5, 8], [-13, 6, 7], [-12, -2, 14], [-12, -1, 13], [-12, 0, 12], [-12, 1, 11], [-12, 2, 10], [-12, 3, 9], [-12, 4, 8], [-12, 5, 7], [-12, 6, 6], [-11, -3, 14], [-11, -2, 13], [-11, -1, 12], [-11, 0, 11], [-11, 1, 10], [-11, 2, 9], [-11, 3, 8], [-11, 4, 7], [-11, 5, 6], [-10, -4, 14], [-10, -3, 13], [-10, -2, 12], [-10, -1, 11], [-10, 0, 10], [-10, 1, 9], [-10, 2, 8], [-10, 3, 7], [-10, 4, 6], [-10, 5, 5], [-9, -5, 14], [-9, -4, 13], [-9, -3, 12], [-9, -2, 11], [-9, -1, 10], [-9, 0, 9], [-9, 1, 8], [-9, 2, 7], [-9, 3, 6], [-9, 4, 5], [-8, -6, 14], [-8, -5, 13], [-8, -4, 12], [-8, -3, 11], [-8, -2, 10], [-8, -1, 9], [-8, 0, 8], [-8, 1, 7], [-8, 2, 6], [-8, 3, 5], [-8, 4, 4], [-7, -7, 14], [-7, -6, 13], [-7, -5, 12], [-7, -4, 11], [-7, -3, 10], [-7, -2, 9], [-7, -1, 8], [-7, 0, 7], [-7, 1, 6], [-7, 2, 5], [-7, 3, 4], [-6, -6, 12], [-6, -5, 11], [-6, -4, 10], [-6, -3, 9], [-6, -2, 8], [-6, -1, 7], [-6, 0, 6], [-6, 1, 5], [-6, 2, 4], [-6, 3, 3], [-5, -5, 10], [-5, -4, 9], [-5, -3, 8], [-5, -2, 7], [-5, -1, 6], [-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-4, -4, 8], [-4, -3, 7], [-4, -2, 6], [-4, -1, 5], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-3, -3, 6], [-3, -2, 5], [-3, -1, 4], [-3, 0, 3], [-3, 1, 2], [-2, -2, 4], [-2, -1, 3], [-2, 0, 2], [-2, 1, 1], [-1, -1, 2], [-1, 0, 1], [0, 0, 0]])


if __name__ == "__main__":
    main()