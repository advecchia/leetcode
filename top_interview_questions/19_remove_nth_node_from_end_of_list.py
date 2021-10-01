# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import List, Optional
import unittest

# MINIMUM_NODE_LIST_LENGTH = 1 # not necessary
MAXIMUM_NODE_LIST_LENGTH = 30
MINIMUM_N_VALUE = 1
MINIMUM_NODE_VALUE = 0
MAXIMUM_NODE_VALUE = 100

class SolutionValidator(object):
    def validate_node_value(self, value: int) -> None:
        if MINIMUM_NODE_VALUE > value or value > MAXIMUM_NODE_VALUE:
            raise ValueError('Invalid node value')

    def validate_node_list_length(self, node_list_len: int) -> None:
        if node_list_len > MAXIMUM_NODE_LIST_LENGTH:
            raise ValueError('Invalid node list length')

    def validate_min_n_value(self, n: int) -> None:
        if MINIMUM_N_VALUE > n:
            raise ValueError('Invalid n value')

    def validate_max_n_value(self, n: int, node_list_len: int) -> None:
        if n > node_list_len:
            raise ValueError('Invalid n value')


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        """ Given the head of a linked list, 
            remove the nth node from the end of the list 
            and return its head.

            Follow up: Could you do this in one pass?
        """
        self.validator = SolutionValidator()

    def removeNthFromEnd_two_pass(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ Two pass solution
        """
        # Basic validations
        if not head or type(head) != ListNode:
            raise ValueError('Invalid head')

        self.validator.validate_min_n_value(n)

        node_list_len = 0
        head_pointer = head
        n_pointer = None
        while head_pointer:
            node_list_len += 1
            self.validator.validate_node_value(head_pointer.val)
            head_pointer = head_pointer.next

        self.validator.validate_max_n_value(n, node_list_len)

        if node_list_len == 1:
            return None

        head_pointer = head
        if node_list_len == n:
            # Remove first node
            head = head.next
            return head

        while node_list_len - 1 > n:
            node_list_len -= 1
            head_pointer = head_pointer.next

        if head_pointer.next:
            head_pointer.next = head_pointer.next.next

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ One pass solution
        """
        # Basic validations
        if not head or type(head) != ListNode:
            raise ValueError('Invalid head')

        self.validator.validate_min_n_value(n)

        # Keep all the pointer like a breadcrumb flag
        pointer_memory = {}
        node_list_len = 1
        head_pointer = head

        while head_pointer.next:
            # Move pointers through the node list
            self.validator.validate_node_value(head_pointer.val)
            pointer_memory[node_list_len] = head_pointer
            head_pointer, node_list_len = head_pointer.next, node_list_len + 1

        self.validator.validate_max_n_value(n, node_list_len)

        to_remove_index = node_list_len - n
        if to_remove_index == 0:
            # Remove first node
            head = head.next
            return head

        if to_remove_index in pointer_memory:
            pointer_memory[to_remove_index].next = pointer_memory[to_remove_index].next.next
            return head


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
    tc.assertEqual(extract_list(sol.removeNthFromEnd(make_typing_list([1,2,3,4,5]), 2)), [1,2,3,5])

    print('Example 2')
    tc.assertEqual(extract_list(sol.removeNthFromEnd(make_typing_list([1]), 1)), [])

    print('Example 3')
    tc.assertEqual(extract_list(sol.removeNthFromEnd(make_typing_list([1,2]), 1)), [1])

    print('Example 4')
    tc.assertEqual(extract_list(sol.removeNthFromEnd(make_typing_list([2,1]), 2)), [1])

    print('Example 5')
    tc.assertEqual(extract_list(sol.removeNthFromEnd(make_typing_list([1,2]), 2)), [2])

    print('Example 6')
    tc.assertEqual(extract_list(sol.removeNthFromEnd(make_typing_list([1,2,3,4]), 4)), [2,3,4])

    print('Example 7')
    tc.assertEqual(extract_list(sol.removeNthFromEnd(make_typing_list([1,2,3,4]), 1)), [1,2,3])


if __name__ == "__main__":
    main()