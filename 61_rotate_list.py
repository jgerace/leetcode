"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 10^9
"""
from typing import Optional

from testing import listNodeToList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # note that k could be greater than the length of the list this sets k to the actual
        # number of spaces we need to rotate in the event that we are asked to rotate a number
        # of spaces greater than the list length
        listLen = 0
        ptr = head
        while ptr is not None:
            listLen += 1
            ptr = ptr.next
        k %= listLen

        # get the k-th element from the end of the list this is the new list tail
        # in order to do this we will have to advance a pointer k spaces forward
        # and get a second pointer to trail behind it. this initializes the leading pointer
        endPtr = head
        for idx in range(k):
            endPtr = endPtr.next

        newTailPtr = head
        while endPtr.next is not None:
            endPtr = endPtr.next
            newTailPtr = newTailPtr.next

        # the current tail of the list needs to point to the current head
        endPtr.next = head

        # whatever the new tail points to will become the new head
        head = newTailPtr.next

        # the newTail must then point to a next node of None since it's the end of the new list
        newTailPtr.next = None

        return head


if __name__ == "__main__":
    input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    output = Solution().rotateRight(input, 2)
    assert listNodeToList(output) == [4, 5, 1, 2, 3]

    input = ListNode(0, ListNode(1, ListNode(2)))
    output = Solution().rotateRight(input, 4)
    assert listNodeToList(output) == [2, 0, 1]

    input = ListNode(0, ListNode(1, ListNode(2)))
    output = Solution().rotateRight(None, 4)
    assert output is None

    input = ListNode(0)
    output = Solution().rotateRight(input, 4)
    assert listNodeToList(output) == [0]
