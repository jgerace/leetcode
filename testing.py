from typing import List


def listItemsEqual(one, two) -> bool:
    if len(one) != len(two):
        return False

    for ii in range(len(one)):
        try:
            two.index(one[ii])
        except ValueError:
            return False
    return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listNodeToList(head: ListNode) -> List[int]:
    output = []
    while head is not None:
        output.append(head.val)
        head = head.next
    return output
