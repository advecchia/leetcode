# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional
import math
import unittest

MAXIMUM_K_LIST_LENGTH = 10**4
MAXIMUM_INNER_LIST_LENGTH = 500
MINIMUM_ELEMENT_VALUE = -10**4
MAXIMUM_ELEMENT_VALUE = 10**4

class SolutionValidator(object):
    def validate_k_list_length(self, list_len: int) -> None:
        if list_len > MAXIMUM_K_LIST_LENGTH:
            raise ValueError('Invalid k lists length')

    def validate_inner_list_length(self, list_len: int) -> None:
        if list_len > MAXIMUM_INNER_LIST_LENGTH:
            raise ValueError('Invalid list length')

    def validate_element_value(self, element_value: int) -> None:
        if MINIMUM_ELEMENT_VALUE > element_value or element_value > MAXIMUM_ELEMENT_VALUE:
            raise ValueError('Invalid element value')


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        """ You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
            Merge all the linked-lists into one sorted linked-list and return it.
        """
        self.validator = SolutionValidator()

    def mergeTwoLists(self, left: List[Optional[ListNode]], right: List[Optional[ListNode]]) -> Optional[ListNode]:
        len_left = len(left)
        if len_left > 1:
            parts = math.floor(len_left/2)
            l1 = self.mergeTwoLists(left[:parts], left[parts:])
        else:
            l1 = left.pop()

        len_right = len(right)
        if len_right > 1:
            parts = math.floor(len_right/2)
            l2 = self.mergeTwoLists(right[:parts], right[parts:])
        else:
            l2 = right.pop()

        l1_head = l1
        l1_len = 0
        l2_head = l2
        l2_len = 0
        output_head = ListNode()
        output_pointer = output_head

        while l1_head and l2_head:
            if l1_head.val <= l2_head.val:
                self.validator.validate_element_value(l1_head.val)
                l1_len += 1
                output_pointer.next = l1_head
                output_pointer = output_pointer.next
                l1_head = l1_head.next

            else:
                self.validator.validate_element_value(l2_head.val)
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

        #self.validator.validate_inner_list_length(l1_len)
        #self.validator.validate_inner_list_length(l2_len)

        # Ignore head value and point to right start node
        output_head = output_head.next
        return output_head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Basic validations
        if not lists:
            return None

        len_lists = len(lists)
        self.validator.validate_k_list_length(len_lists)

        if len_lists == 1:
            return lists[0]

        parts = math.floor(len_lists/2)
        return self.mergeTwoLists(lists[:parts], lists[parts:])


def make_typing_list(values: []) -> List[Optional[ListNode]]:    
    output = []
    for i in range(len(values)):
        values[i].reverse()
        head = None
        last = None
        for j in range(len(values[i])):
            head = ListNode(values[i][j], last)
            last = head

        output.append(head)

    return output

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
    tc.assertEqual(extract_list(sol.mergeKLists(make_typing_list([[1,4,5],[1,3,4],[2,6]]))), [1,1,2,3,4,4,5,6])

    print('Example 2')
    tc.assertEqual(extract_list(sol.mergeKLists(make_typing_list([]))), [])

    print('Example 3')
    tc.assertEqual(extract_list(sol.mergeKLists(make_typing_list([[]]))), [])


if __name__ == "__main__":
    main()