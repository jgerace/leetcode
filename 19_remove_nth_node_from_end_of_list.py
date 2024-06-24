"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""
from typing import Optional

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        dummy_head = ListNode(-1, head)
        end_ptr = dummy_head
        target_ptr = head
        prev_ptr = dummy_head
        for idx in range(n):
            end_ptr = end_ptr.next

        while end_ptr.next is not None:
            end_ptr = end_ptr.next
            target_ptr = target_ptr.next
            prev_ptr = prev_ptr.next
        prev_ptr.next = target_ptr.next

        return dummy_head.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output = Solution().removeNthFromEnd(head, 2)
    assert listNodeToList(output) == [1, 2, 3, 5]

    head = ListNode(1)
    output = Solution().removeNthFromEnd(head, 1)
    assert listNodeToList(output) == []

    head = ListNode(1, ListNode(2))
    output = Solution().removeNthFromEnd(head, 1)
    assert listNodeToList(output) == [1]
