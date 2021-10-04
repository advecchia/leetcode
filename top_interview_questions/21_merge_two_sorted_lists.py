# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import List, Optional
import unittest

MINIMUM_NODE_VALUE = -100
MAXIMUM_NODE_VALUE = 100
# MINIMUM_LIST_LENGTH = 0 # not necessary
MAXIMUM_LIST_LENGTH = 50

class SolutionValidator(object):
    def validate_node_value(self, node_value: int) -> None:
        if MINIMUM_NODE_VALUE > node_value or node_value > MAXIMUM_NODE_VALUE:
            raise ValueError('Invalid node value')

    def validate_list_length(self, list_len: int) -> None:
        if list_len > MAXIMUM_LIST_LENGTH:
            raise ValueError('Invalid list length')


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        """ Merge two sorted linked lists and return it as a sorted list. 
            The list should be made by splicing together the nodes of the first two lists.

            Constraints:
            - Both l1 and l2 are sorted in non-decreasing order.
        """
        self.validator = SolutionValidator()

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Basic validations
        if not l1:
            return l2

        if not l2:
            return l1

        l1_head = l1
        l1_len = 0
        l2_head = l2
        l2_len = 0
        output_head = ListNode()
        output_pointer = output_head

        while l1_head and l2_head:
            if l1_head.val <= l2_head.val:
                self.validator.validate_node_value(l1_head.val)
                l1_len += 1
                output_pointer.next = l1_head
                output_pointer = output_pointer.next
                l1_head = l1_head.next

            else:
                self.validator.validate_node_value(l2_head.val)
                l2_len += 1
                output_pointer.next = l2_head
                output_pointer = output_pointer.next
                l2_head = l2_head.next

        if l1_head:
            output_pointer.next = l1_head
            while l1_head:
                l1_len += 1
                l1_head = l1_head.next
        else:
            output_pointer.next = l2_head
            while l2_head:
                l2_len += 1
                l2_head = l2_head.next

        self.validator.validate_list_length(l1_len)
        self.validator.validate_list_length(l2_len)

        # Ignore head value and point to right start node
        output_head = output_head.next
        return output_head


def make_typing_list(values: []) -> Optional[ListNode]:
    values.reverse()
    head = None
    last = None
    for i in range(len(values)):
        head = ListNode(values[i], last)
        last = head

    return head

def extract_list(head: Optional[ListNode]) -> []:
    output = []
    while head:
        output.append(head.val)
        head = head.next

    return output

def main():
    tc = unittest.TestCase()
    sol = Solution()

    print('Example 1')
    tc.assertEqual(extract_list(sol.mergeTwoLists(make_typing_list([1,2,4]), make_typing_list([1,3,4]))), [1,1,2,3,4,4])

    print('Example 2')
    tc.assertEqual(extract_list(sol.mergeTwoLists(make_typing_list([]), make_typing_list([]))), [])

    print('Example 3')
    tc.assertEqual(extract_list(sol.mergeTwoLists(make_typing_list([]), make_typing_list([0]))), [0])

    print('Example 4')
    tc.assertEqual(extract_list(sol.mergeTwoLists(make_typing_list([3,4,5,6,7]), make_typing_list([]))), [3,4,5,6,7])

    print('Example 5')
    tc.assertEqual(extract_list(sol.mergeTwoLists(make_typing_list([]), make_typing_list([7,8,9,10]))), [7,8,9,10])

    print('Example 6')
    tc.assertEqual(extract_list(sol.mergeTwoLists(make_typing_list([1,2,3,4]), make_typing_list([5,6,7,8]))), [1,2,3,4,5,6,7,8])

    print('Example 7')
    tc.assertEqual(extract_list(sol.mergeTwoLists(make_typing_list([5,6,7,8]), make_typing_list([1,2,3,4]))), [1,2,3,4,5,6,7,8])

    print('Example 8')
    tc.assertEqual(extract_list(sol.mergeTwoLists(make_typing_list([1,1,1,2,3,3,3]), make_typing_list([1,2,2,2,3]))), [1,1,1,1,2,2,2,2,3,3,3,3])


if __name__ == "__main__":
    main()