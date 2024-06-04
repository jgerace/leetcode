"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional, List

from testing import listNodeToList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1ptr = l1
        l2ptr = l2

        output = ListNode(0)
        outputPtr = output
        carry = 0
        while not (l1ptr is None and l2ptr is None):
            l1Val = 0
            l2Val = 0
            if l1ptr is not None:
                l1Val = l1ptr.val
                l1ptr = l1ptr.next
            if l2ptr is not None:
                l2Val = l2ptr.val
                l2ptr = l2ptr.next

            total = l1Val + l2Val + carry
            if total > 9:
                carry = 1
                total %= 10
            else:
                carry = 0

            outputPtr.next = ListNode(total)
            outputPtr = outputPtr.next

        if carry != 0:
            outputPtr.next = ListNode(carry)

        return output.next


if __name__ == "__main__":
    head1 = ListNode(2, ListNode(4, ListNode(3)))
    head2 = ListNode(5, ListNode(6, ListNode(4)))
    output = Solution().addTwoNumbers(head1, head2)
    assert listNodeToList(output) == [7, 0, 8]

    head1 = ListNode(0)
    head2 = ListNode(0)
    output = Solution().addTwoNumbers(head1, head2)
    assert listNodeToList(output) == [0]

    head1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    head2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    output = Solution().addTwoNumbers(head1, head2)
    assert listNodeToList(output) == [8, 9, 9, 9, 0, 0, 0, 1]
