"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output = Solution().reverseList(head)
    assert listNodeToList(output) == [5, 4, 3, 2, 1]

    head = ListNode(1, ListNode(2))
    output = Solution().reverseList(head)
    assert listNodeToList(output) == [2, 1]

    output = Solution().reverseList(None)
    assert listNodeToList(output) == []

    head = ListNode(1)
    output = Solution().reverseList(head)
    assert listNodeToList(output) == [1]
