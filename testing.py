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
