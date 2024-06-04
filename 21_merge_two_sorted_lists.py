"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # short circuit for efficiency
        if list1 is None and list2 is None:
            return None
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is not None:
            return list2

        ptr1 = list1
        ptr2 = list2

        output = ListNode(0, None)
        outputPtr = output
        while ptr1 is not None or ptr2 is not None:
            if ptr1 is not None and ptr2 is not None:
                if ptr1.val < ptr2.val:
                    outputPtr.next = ListNode(ptr1.val)
                    ptr1 = ptr1.next
                else:
                    outputPtr.next = ListNode(ptr2.val)
                    ptr2 = ptr2.next
                outputPtr = outputPtr.next
            elif ptr1 is not None:
                outputPtr.next = ptr1
                return output.next
            else:
                outputPtr.next = ptr2
                return output.next


def listNodeToList(head: ListNode) -> List[int]:
    output = []
    while head is not None:
        output.append(head.val)
        head = head.next
    print(output)
    return output


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(4)))
    head2 = ListNode(1, ListNode(3, ListNode(4)))
    output = Solution().mergeTwoLists(head1, head2)
    assert listNodeToList(output) == [1, 1, 2, 3, 4, 4]

    output = Solution().mergeTwoLists(None, None)
    assert output is None

    head2 = ListNode(0)
    output = Solution().mergeTwoLists(None, head2)
    assert output.val == 0 and output.next is None

    head1 = ListNode(0)
    output = Solution().mergeTwoLists(head1, None)
    assert output.val == 0 and output.next is None

    head1 = ListNode(1, ListNode(3, ListNode(5)))
    head2 = ListNode(2, ListNode(4, ListNode(6)))
    output = Solution().mergeTwoLists(head1, head2)
    assert listNodeToList(output) == [1, 2, 3, 4, 5, 6]
