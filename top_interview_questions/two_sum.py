MINIMUM_VALUE = -10**9
MAXIMUM_VALUE = 10**9
MINIMUM_LIST_SIZE = 2
MAXIMUM_LIST_SIZE = 10**4

class SolutionValidator:
    def validate_int(self, num: int):
        if MINIMUM_VALUE > num > MAXIMUM_VALUE:
            raise ValueError("Number exceeds correct values")

    def validate_list_size(self, size: int):
        if MINIMUM_LIST_SIZE > size > MAXIMUM_LIST_SIZE:
            raise ValueError("Size exceeds correct values")


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        validator = SolutionValidator()
        validator.validate_int(target)
        validator.validate_list_size(len(nums))

        # Validate first number, the rest will be validate inside iteration
        validator.validate_int(nums[0])
        for i in range(len(nums)):
            # Validate pivot
            validator.validate_int(nums[i])
            for j in range(i+1, len(nums)):
                # Validate pair
                validator.validate_int(j)
                if nums[i] + nums[j] == target:
                    return [i, j]


def main():
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))
    print(sol.twoSum([3,2,4], 6))
    print(sol.twoSum([3,3], 6))


if __name__ == "__main__":
    main()