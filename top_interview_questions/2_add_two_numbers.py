# https://leetcode.com/problems/add-two-numbers/
from typing import Optional
import functools
import unittest
MINIMUM_NODE_VALUE = 0
MAXIMUM_NODE_VALUE = 9
MINIMUM_LINKED_LIST_SIZE = 1
MAXIMUM_LINKED_LIST_SIZE = 100

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionValidator(object):
    def validate_node_value(self, value: int) -> None:
        if MINIMUM_NODE_VALUE > value > MAXIMUM_NODE_VALUE:
            raise ValueError('Invalid node value')

    def validate_linked_list_size(self, size: int) -> None:
        if MINIMUM_LINKED_LIST_SIZE > size > MAXIMUM_LINKED_LIST_SIZE:
            raise ValueError('Invalid size for linked list')

    def is_valid_node(self, linked_list: Optional[ListNode]) -> None:
        if not linked_list:
            raise ValueError('Invalid linked list format')


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        validator = SolutionValidator()
        # validates linked list definiton
        validator.is_valid_node(l1)
        validator.is_valid_node(l2)

        # Sum the number and return the linked list
        first = self.build_number(l1)
        second = self.build_number(l2)
        total = first + second
        return self.build_output(total)

    def build_number(self, linked_list: Optional[ListNode]) -> int:
        """ Run over the linked list, put each value into array, reverse it,
        convert each value to string, join the string and convert to a number.
        Return a number.
        """
        validator = SolutionValidator()
        values = list()
        node = linked_list
        while(node):
            validator.validate_node_value(node.val)
            values.append(node.val)
            node = node.next
        # validates linked list size
        validator.validate_linked_list_size(len(values))

        # build first number
        values.reverse()
        operand = functools.reduce(lambda a,b: str(a)+str(b), values)
        print(operand)
        return int(operand)

    def build_output(self, number: int) -> Optional[ListNode]:
        """ Turn a number into a linked list with reverted order values.
        """
        values = [char for char in str(number)]
        print(values)
        current = None
        for val in values:
            node = ListNode(val, current)
            current = node
        return current

def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    l11 = None
    l12 = ListNode(5, ListNode(6, ListNode(4)))
    with tc.assertRaises(ValueError):
        print(sol.addTwoNumbers(l11, l12))

    print('Example 2')
    l21 = ListNode(5, ListNode(6, ListNode(4)))
    l22 = None
    with tc.assertRaises(ValueError):
        print(sol.addTwoNumbers(l21, l22))

    print('Example 3')
    l31 = ListNode(2, ListNode(4, ListNode(3))) # Input: l31 = [2,4,3], l32 = [5,6,4]
    l32 = ListNode(5, ListNode(6, ListNode(4)))
    print(sol.addTwoNumbers(l31, l32)) # Output: [7,0,8]

    print('Example 4')
    l41 = ListNode(0) # Input: l41 = [0], l42 = [0]
    l42 = ListNode(0)
    print(sol.addTwoNumbers(l41, l42)) # Output: [0]

    print('Example 5')
    l51 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ))))))) # Input: l51 = [9,9,9,9,9,9,9], l52 = [9,9,9,9]
    l52 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    print(sol.addTwoNumbers(l51, l52)) # Output: [8,9,9,9,0,0,0,1]


if __name__ == "__main__":
    main()