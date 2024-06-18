"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []

Constraints:

    The number of nodes in the list is in the range [0, 5 * 10^4].
    -10^5 <= Node.val <= 10^5

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""
import math
from typing import Optional, List

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, first: ListNode, second: ListNode) -> ListNode:
        idx1 = 0
        idx2 = 0
        dummy_head = head = ListNode(0)
        while first or second:
            if not first:
                head.next = second
                head = head.next
                second = second.next
                idx2 += 1
                continue
            elif not second:
                head.next = first
                head = head.next
                first = first.next
                idx1 += 1
                continue

            if first.val < second.val:
                head.next = first
                head = head.next
                first = first.next
                idx1 += 1
            else:
                head.next = second
                head = head.next
                second = second.next
                idx2 += 1

        return dummy_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if head.next is None:
            return head

        if not head or not head.next:
            return head

        def get_mid(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid = get_mid(head)
        second_half_head = mid.next
        mid.next = None

        print("sorting first half")
        first_half = self.sortList(head)
        print("sorting second half")
        second_half = self.sortList(second_half_head)

        print("merging")
        return self.merge(first_half, second_half)


if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    output = Solution().sortList(head)
    assert listNodeToList(output) == [1, 2, 3, 4]

    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    output = Solution().sortList(head)
    assert listNodeToList(output) == [-1, 0, 3, 4, 5]

    output = Solution().sortList(None)
    assert listNodeToList(output) == []
